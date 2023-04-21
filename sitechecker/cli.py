import argparse
import sys
from typing import Sequence
import pathlib

def read_user_cli_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Recebe os comandos do usuário"""
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Este aplicativo testa a conectividade de um ou mais sites através de suas URLs. Para verificar você pode utilizar as opções: "
    ) # classe ArgumentParser que recebe argumentos da linha de comando
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URL", # Define um nome para o argumento em uso
        nargs="+",
        type=str,
        default=[],
        help="insira um ou mais URLs. Ex: python sitecheker -u site.com outrosite.com.br",
    )
    parser.add_argument(
        "-f",
        "--imput-file",
        metavar="FILE",
        # nargs="+", # números de argumentos que podem ser usados
        type=argparse.FileType("r"),
        help="insira um arquivo csv contendo uma ou mais URLs. Ex: python sitechecker -f nomearquivo.csv",
    )
    return parser.parse_args(args)

def get_urls(user_args):
    """Obtém as URLs digitadas ou disponibilizadas em um arquivo csv"""
    urls = []
    urls += user_args.urls
    if user_args.imput_file:
        lines = user_args.imput_file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line for line in lines if line != ""]
        urls += lines
    return urls


def generate_check_results(url, is_online, error) -> str:
    """Gera os resultados da checagem de conexão"""
    start = f'O status da "{url}" é: '
    if is_online:
        return start + '"Online!"'
    else:
        return start + f'"Offline?"\n  Erro: "{error}"'


def display_check_result(url, is_online, error):
    """Imprime os resultados da checagem de conexão"""
    print(generate_check_results(url, is_online, error))



