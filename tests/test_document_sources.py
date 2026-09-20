import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / 'skills/ai-platform-docs/scripts'
sys.path.insert(0, str(SCRIPTS))
import markdown_sources as sources


class ProviderRegistryTests(unittest.TestCase):
    def test_markdown_dispatch_excludes_volcengine_pdf(self):
        config = json.loads((SCRIPTS.parent / 'providers.json').read_text(encoding='utf-8'))
        self.assertEqual([p['key'] for p in config['providers']], ['volcengine', 'kling', 'minimax'])
        self.assertEqual([p['key'] for p in sources.providers()], ['kling', 'minimax'])

    def test_fetch_uses_registry_library_ids_and_products(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            scripts = root / 'scripts'
            scripts.mkdir()
            for name in ('products.py', 'fetch_docs.py'):
                shutil.copy2(SCRIPTS / name, scripts / name)
            config = {'providers': [{'key': 'volcengine', 'type': 'volcengine-pdf',
                                    'library_ids': [123456], 'products': [{'key': 'fixture', 'source': 'fixture'}]}]}
            (root / 'providers.json').write_text(json.dumps(config), encoding='utf-8')
            probe = '''import sys
import fetch_docs
def discover(ids):
    assert ids == [123456], ids
    return [{'source_name': 'fixture', 'has_update': False, 'local_ts': 1, 'remote_ts': 1}]
fetch_docs.discover_available_pdfs = discover
sys.argv = ['fetch_docs.py', '--check']
fetch_docs.main()
'''
            (scripts / 'probe.py').write_text(probe, encoding='utf-8')
            result = subprocess.run([sys.executable, str(scripts / 'probe.py')], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_status_checks_each_volcengine_zone(self):
        sys.path.insert(0, str(ROOT / 'scripts'))
        from validation import documentation_status
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / 'skills/ai-platform-docs'
            output = skill / 'generated'
            (output / 'chapters/volcengine/tos').mkdir(parents=True)
            for name in ('INDEX.md', 'INDEX-tos.md', 'chapters/volcengine/tos/page.md'):
                (output / name).write_text('# Fixture', encoding='utf-8')
            config = {'providers': [{'key': 'volcengine', 'type': 'volcengine-pdf', 'products': [{'key': 'tos'}]}]}
            (skill / 'providers.json').write_text(json.dumps(config), encoding='utf-8')
            files = {p.relative_to(output).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in output.rglob('*') if p.is_file()}
            manifest = {'layout_version': 2, 'files': files, 'sources': {'volcengine': {'zones': 1}}, 'built_at': 'fixture', 'origin': 'fixture'}
            (output / 'snapshot.json').write_text(json.dumps(manifest), encoding='utf-8')
            self.assertTrue(documentation_status(root)['ready'])
            config['providers'][0]['products'][0]['key'] = 'ark'
            (skill / 'providers.json').write_text(json.dumps(config), encoding='utf-8')
            result = documentation_status(root)
            self.assertFalse(result['ready'])
            self.assertIn('volcengine/ark', result['reason'])


class MarkdownSourcesTests(unittest.TestCase):
    def setUp(self):
        self.provider = {'key': 'example', 'label': 'Fixture API', 'region': 'fixture',
                         'index_url': 'https://docs.example/llms.txt', 'hosts': ['docs.example'],
                         'include_paths': ['/api/'], 'required_paths': ['/api/auth.md']}
        self.body = '# API\n\n| Parameter | Required |\n|---|---|\n| prompt | Yes |\n\n```json\n{"prompt": "keep code and tables intact"}\n```\n'
        self.index = '- [Authentication](https://docs.example/api/auth.md)\n- [Video](https://docs.example/api/video.md)\n'

    def test_windows_download_hash_matches_bytes_and_markdown_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            cache, output = Path(temp) / 'cache', Path(temp) / 'generated'
            def fetch(url, provider):
                return self.index if url.endswith('llms.txt') else self.body
            with patch.object(sources, 'fetch_text', side_effect=fetch):
                sources.fetch_provider(self.provider, cache)
            metadata = sources.load_provider(self.provider, cache)
            summary = sources.build_provider(self.provider, cache, output)
            self.assertEqual(summary['pages'], 2)
            for row in metadata['pages']:
                raw = (cache / 'example' / row['file']).read_bytes()
                self.assertEqual(raw, self.body.encode())
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row['sha256'])
                self.assertTrue((output / 'chapters/example' / row['file']).read_text(encoding='utf-8').endswith(self.body))
            (cache / 'example' / metadata['pages'][0]['file']).write_text('truncated')
            with self.assertRaisesRegex(ValueError, 'modified source'):
                sources.load_provider(self.provider, cache)

    def test_catalog_changes_remove_retired_pages_from_next_build(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / 'cache'
            def fetch(url, provider):
                return self.index if url.endswith('llms.txt') else self.body
            with patch.object(sources, 'fetch_text', side_effect=fetch):
                before = sources.fetch_provider(self.provider, cache)
                self.index = self.index.splitlines()[0] + '\n'
                after = sources.fetch_provider(self.provider, cache)
            self.assertEqual(len(after['pages']), 1)
            self.assertNotEqual(sources.fingerprint_rows(before), sources.fingerprint_rows(after))
            self.assertEqual(len(list((cache / 'example').glob('*.md'))), 1)
            self.assertEqual(sources.build_provider(self.provider, cache, Path(temp) / 'next')['pages'], 1)

    def test_incomplete_or_foreign_catalog_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Incomplete'):
            sources.catalog('- [Video](https://docs.example/api/video.md)', self.provider)
        with self.assertRaisesRegex(ValueError, 'Unexpected document URL'):
            sources.catalog(self.index + '- [Foreign](https://other.example/api/page.md)', self.provider)


class BuildTransactionTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / '.cache/tests'
        base.mkdir(parents=True, exist_ok=True)
        self.base = base.resolve()
        self.tempdir = tempfile.TemporaryDirectory(prefix='docs-', dir=base)
        self.temp = Path(self.tempdir.name).resolve()
        self.cache, self.live = self.temp / '.cache', self.temp / 'generated'
        (self.cache / 'work/doc').mkdir(parents=True)
        self.source = self.cache / 'work/doc/source.md'
        self.source.write_text('Original fixture text', encoding='utf-8')
        (self.temp / 'providers.json').write_text('{"providers": []}', encoding='utf-8')
        spec = importlib.util.spec_from_file_location('transaction_builder', SCRIPTS / 'build_all.py')
        self.builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.builder)
        self.builder.CACHE, self.builder.LIVE, self.builder.SKILL_ROOT = self.cache, self.live, self.temp
        self.builder.PRODUCTS = [{'key': 'tos', 'source': 'source'}]
        self.builder.providers = lambda: []
        self.builder.run = self.fake_pipeline
        self.args = argparse.Namespace(import_from=None, fetch=False, convert=False, only=None, if_changed=True, oversize=1500)

    def tearDown(self):
        self.assertTrue(self.temp.is_relative_to(self.base))
        self.tempdir.cleanup()

    def fake_pipeline(self, script, *args, work):
        # This fixture tests publication/rollback, not the PDF parser.
        if script == 'build_volc_doc_skill.py':
            chapter = work / 'generated/chapters/volcengine/tos/page.md'
            chapter.parent.mkdir(parents=True)
            chapter.write_text((work / 'doc/source.md').read_text(encoding='utf-8'), encoding='utf-8')
        elif script == 'gen_index.py':
            (work / 'generated/INDEX.md').write_text('# Fixture index', encoding='utf-8')

    def test_unchanged_inputs_skip_rebuild_and_modified_snapshot_is_repaired(self):
        self.assertTrue(self.builder.build(self.args)['rebuilt'])
        before = (self.live / 'snapshot.json').read_bytes()
        self.assertEqual(self.builder.build(self.args)['status'], 'unchanged')
        self.assertEqual((self.live / 'snapshot.json').read_bytes(), before)
        (self.live / 'chapters/volcengine/tos/page.md').write_text('tampered')
        self.assertTrue(self.builder.build(self.args)['rebuilt'])
        self.assertEqual((self.live / 'chapters/volcengine/tos/page.md').read_text(), 'Original fixture text')
        self.source.write_text('Updated fixture text')
        self.assertTrue(self.builder.build(self.args)['rebuilt'])
        self.assertEqual((self.live / 'chapters/volcengine/tos/page.md').read_text(), 'Updated fixture text')

    def test_failed_provider_download_preserves_snapshot_and_cache(self):
        self.builder.build(self.args)
        before = (self.live / 'snapshot.json').read_bytes()
        self.args.fetch = True
        self.builder.providers = lambda: [{'key': 'example'}]
        with patch.object(self.builder, 'fetch_provider', side_effect=ConnectionError('fixture network failure')):
            with self.assertRaises(ConnectionError):
                self.builder.build(self.args)
        self.assertEqual((self.live / 'snapshot.json').read_bytes(), before)
        self.assertEqual(self.source.read_text(), 'Original fixture text')
        self.assertEqual(list(self.cache.glob('build-*')), [])

    def test_failed_publish_restores_both_cache_and_snapshot(self):
        self.builder.build(self.args)
        before = (self.live / 'snapshot.json').read_bytes()
        self.source.write_text('Pending source update')
        original_replace = os.replace
        def fail_publish(source, destination):
            if Path(destination) == self.live and Path(source).name == 'generated':
                raise OSError('fixture publish failure')
            return original_replace(source, destination)
        with patch.object(self.builder.os, 'replace', side_effect=fail_publish):
            with self.assertRaises(OSError):
                self.builder.build(self.args)
        self.assertEqual((self.live / 'snapshot.json').read_bytes(), before)
        self.assertEqual(self.source.read_text(), 'Pending source update')


if __name__ == '__main__':
    unittest.main()
