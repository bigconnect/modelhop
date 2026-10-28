# modelhop

Send one prompt to any OpenAI-compatible provider from the command line. No dependencies.

```sh
export OPENROUTER_API_KEY=*** -m modelhop --provider openrouter --model openai/gpt-4o-mini "Say hi"
```

## Supported providers

| Provider | `--provider` | Key variable |
|---|---|---|
| DeepInfra | `deepinfra` | `DEEPINFRA_API_KEY` |
| Groq | `groq` | `GROQ_API_KEY` |
| llm.buzz | `llmbuzz` | `LLM_BUZZ_API_KEY` |
| OpenAI | `openai` | `OPENAI_API_KEY` |
| OpenRouter | `openrouter` | `OPENROUTER_API_KEY` |
| Together AI | `together` | `TOGETHER_API_KEY` |

Missing one? See [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-provider). New providers are welcome.

## License

MIT
