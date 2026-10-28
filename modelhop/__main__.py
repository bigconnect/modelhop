import argparse

from .client import chat
from .providers import PROVIDERS


def main() -> None:
    parser = argparse.ArgumentParser(prog="modelhop")
    parser.add_argument("--provider", choices=sorted(PROVIDERS), default="openrouter")
    parser.add_argument("--model", required=True)
    parser.add_argument("prompt")
    args = parser.parse_args()
    print(chat(args.provider, args.model, args.prompt))


if __name__ == "__main__":
    main()
