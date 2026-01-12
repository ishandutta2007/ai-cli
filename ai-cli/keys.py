import json
from pathlib import Path

KEYS_PATH = Path.home() / ".ai-cli_keys.json"

def set_key(provider: str, value: str | None):
    keys = KEYS_PATH.read_text() if KEYS_PATH.exists() else "{}"
    data = json.loads(keys)
    if value is None:
        data.pop(provider, None)
    else:
        data[provider] = value
    KEYS_PATH.write_text(json.dumps(data, indent=2))

def get_key(provider: str) -> str | None:
    if not KEYS_PATH.exists():
        return None
    data = json.loads(KEYS_PATH.read_text())
    return data.get(provider)