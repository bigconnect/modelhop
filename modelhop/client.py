import json
import os
import urllib.request

from .providers import PROVIDERS


def chat(provider: str, model: str, prompt: str) -> str:
    p = PROVIDERS[provider]
    key = os.environ[p.api_key_env]
    body = json.dumps(
        {"model": model, "messages": [{"role": "user", "content": prompt}]}
    ).encode()
    req = urllib.request.Request(
        f"{p.base_url}/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["choices"][0]["message"]["content"]
