"""Provider registry.

Each entry maps a provider id to its OpenAI-compatible base URL and the
environment variable that holds its API key. Keep entries sorted by id.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Provider:
    name: str
    base_url: str
    api_key_env: str


PROVIDERS: dict[str, Provider] = {
    "deepinfra": Provider(
        name="DeepInfra",
        base_url="https://api.deepinfra.com/v1/openai",
        api_key_env="DEEPINFRA_API_KEY",
    ),
    "groq": Provider(
        name="Groq",
        base_url="https://api.groq.com/openai/v1",
        api_key_env="GROQ_API_KEY",
    ),
    "llmbuzz": Provider(
        name="llm.buzz",
        base_url="https://api.llm.buzz/api/v1",
        api_key_env="LLM_BUZZ_API_KEY",
    ),
    "openai": Provider(
        name="OpenAI",
        base_url="https://api.openai.com/v1",
        api_key_env="OPENAI_API_KEY",
    ),
    "openrouter": Provider(
        name="OpenRouter",
        base_url="https://openrouter.ai/api/v1",
        api_key_env="OPENROUTER_API_KEY",
    ),
    "together": Provider(
        name="Together AI",
        base_url="https://api.together.xyz/v1",
        api_key_env="TOGETHER_API_KEY",
    ),
}
