# Contributing

## Adding a provider

New OpenAI-compatible providers are welcome. One provider per PR:

1. Add an entry to `modelhop/providers.py`. Keep the dict sorted by id.
2. Add a row to the providers table in `README.md`, same order.
3. Add a line under `## Unreleased` in `CHANGELOG.md`.

## Commits

We use Conventional Commits, e.g. `feat(providers): add Groq`.
