"""Replace credential-shaped examples before a snapshot can be published."""
import re

PATTERNS = (
    (re.compile(r'\b(?:AKLT|AKTP)[A-Za-z0-9]+'), '<VOLCENGINE_ACCESS_KEY_ID>'),
    (re.compile(r'(?i)(X-Tos-(?:Security-Token|Signature)=)[^&\s"\x27<>]+'), r'\1<REDACTED_TOS_AUTH_PARAMETER>'),
    (re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'), '<AWS_ACCESS_KEY_ID>'),
    (re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b'), '<GITHUB_TOKEN>'),
    (re.compile(r'\bsk-[A-Za-z0-9_-]{20,}'), '<API_KEY>'),
    (re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+'), '<JWT_TOKEN>'),
    (re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----.*?-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', re.S), '<PRIVATE_KEY>'),
)


def redact(folder):
    count = 0
    for path in folder.rglob('*.md'):
        original = path.read_bytes().decode('utf-8')
        text = original
        for pattern, placeholder in PATTERNS:
            text, matches = pattern.subn(placeholder, text)
            count += matches
        if text != original:
            path.write_bytes(text.encode('utf-8'))
    return {'policy': 'credential-examples-v1', 'replacements': count}
