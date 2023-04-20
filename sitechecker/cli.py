import argparse
import sys
from typing import Sequence
import pathlib

def read_user_cli_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    ) # classe ArgumentParser que recebe argumentos da linha de comando
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs", # define um nome para o argumento em uso
        nargs="+",
        type=str,
        default=[],
        help="insira um ou mais URLs",
    )
    parser.add_argument(
        "-f",
        "--imput-file",
        metavar="file",
        # nargs="+", # números de argumentos que podem ser usados
        type=argparse.FileType("r"),
        help="insira um arquivo csv contendo uma ou mais URLs",
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

def get_urls(user_args):
    urls = []
    urls += user_args.urls
    if user_args.imput_file:
        lines = user_args.imput_file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line for line in lines if line != ""]
        urls += lines
    return urls

# def _read_urls_from_file(file):
#     file_path = pathlib.Path(file)
#     with file_path.is_file():
#         urls = [url.strip() for url in urls_file]
#         if urls:
#             return urls
#             print(f"Error: empty file, {file}", file= sys.stderr)
#         else:
#             print("Error: input file not found", file= sys.stderr)
#         return []
