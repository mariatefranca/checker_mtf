import argparse
from typing import Sequence


def read_user_cli_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    ) # classe ArgumentParser que recebe argumentos da linha de comando
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="insira um ou mais URLs",
    )
    return parser.parse_args(args)


def display_check_result(url, is_online, error):
    """Display the result of a connectivity check."""
    print(generate_check_results(url, is_online, error))


def generate_check_results(url, is_online, error) -> str:
    start = f'O status da "{url}" é: '
    if is_online:
        return start + '"Online!"'
    else:
        return start + f'"Offline?"\n  Erro: "{error}"'


