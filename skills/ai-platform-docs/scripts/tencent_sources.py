"""Read Tencent Cloud's catalog and public document viewer responses as JSON."""
from __future__ import annotations

import json
import re
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from markdown_sources import allowed_url


def response_data(response):
    try:
        result = json.loads(response)
        if result['code'] != 0:
            raise ValueError('Official document API returned an error')
        return result['data']
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError('Invalid Tencent Cloud document data') from exc


def catalog(response, provider):
    try:
        tree = response_data(response)
        if str(tree['categoryId']) != str(provider['product_id']):
            raise ValueError('Unexpected product')
        pages = {}
        prefix = urlsplit(provider['index_url']).path.rstrip('/') + '/'

        def visit(nodes, parents=()):
            for node in nodes:
                title = (*parents, node['title'])
                if node['type'] == 'page':
                    url = allowed_url(provider['index_url'].rstrip('/') + '/' + str(node['id']), provider)
                    path = urlsplit(url).path
                    if not re.fullmatch(re.escape(prefix) + r'\d+', path) or urlsplit(url).query or urlsplit(url).fragment:
                        raise ValueError('Unexpected product page URL')
                    pages[path] = {'url': url, 'title': ' / '.join(title)}
                elif node['type'] != 'directory':
                    raise ValueError('Unsupported catalog node')
                visit(node.get('children', []), title)

        visit(tree['list'])
        if not pages or not set(provider['required_paths']).issubset(pages):
            raise ValueError('Required pages missing')
        return [pages[path] for path in sorted(pages)]
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"Incomplete official catalog: {provider['key']}: {exc}") from exc


class TencentConverter(MarkdownConverter):
    def convert_table(self, el, text, parent_tags):
        # Markdown cannot represent merged cells. Keep these tables as clean HTML.
        if el.select('[rowspan], [colspan]'):
            return '\n\n' + str(el) + '\n\n'
        return super().convert_table(el, text, parent_tags)

    def convert_pre(self, el, text, parent_tags):
        code = el.get_text()
        fence = '`' * max(3, max((len(m) + 1 for m in re.findall(r'`+', code)), default=3))
        language = next((c.removeprefix('language-') for c in el.get('class', []) if c.startswith('language-')), '')
        return f'\n\n{fence}{language}\n{code}\n{fence}\n\n'


def html_to_markdown(body, url):
    soup = BeautifulSoup(body, 'html.parser')
    for element in soup.select('script, style, svg, button, .code-block-toolbar, [data-slate-zero-width]'):
        element.decompose()
    for element in soup.find_all(['a', 'img']):
        attribute = 'href' if element.name == 'a' else 'src'
        if element.get(attribute):
            element[attribute] = urljoin(url, element[attribute])
    for pre in soup.find_all('pre'):
        # Slate renders each source line as a div, without literal newlines.
        lines = pre.find_all('div', recursive=False)
        code = '\n'.join(line.get_text() for line in lines) if lines else pre.get_text()
        pre.clear()
        pre.append(code)
    for span in soup.find_all('span'):
        span.unwrap()
    for element in soup.find_all(True):
        keep = {'href', 'src', 'alt', 'title', 'rowspan', 'colspan'}
        if element.name == 'pre':
            keep.add('class')
        element.attrs = {key: value for key, value in element.attrs.items() if key in keep}
    return TencentConverter(heading_style='ATX', table_infer_header=True, newline_style='BACKSLASH').convert_soup(soup).strip()


def extract_article(response, url, provider, *, fetch_glossary=None):
    try:
        article = response_data(response)
        content = article['content']
        if (article['type'] != 'page' or str(article['categoryId']) != str(provider['product_id'])
                or content.get('disable')):
            raise ValueError('Unexpected or disabled article')
        if content.get('isGlossary'):
            if fetch_glossary is None:
                raise ValueError('Glossary content requires its public document endpoint')
            glossary = response_data(fetch_glossary())
            content = {**content, 'body': glossary['glossaryContent'], 'markdown': '',
                       'recentReleaseTime': glossary['recentReleaseTime']}
        body = content.get('markdown') or html_to_markdown(content['body'], url)
        if not body.strip() or not content['title'].strip():
            raise ValueError('Empty article')
        updated = content.get('recentReleaseTime', '')
        return f"# {content['title']}\n\n官方来源：{url}\n最近更新时间：{updated}\n\n{body.strip()}\n"
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f'Invalid Tencent Cloud article: {url}: {exc}') from exc
