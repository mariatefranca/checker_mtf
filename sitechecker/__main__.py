import sys

from sitechecker.checker import check_connection
from sitechecker.cli import read_user_cli_args, display_check_result, get_urls


def main():
    """Run Site Checker."""
    user_args = read_user_cli_args() # Recebe os comandos do usuário
    urls = get_urls(user_args) # Retorna as urls dos sites para checagem
    if not urls:
        print("Erro: sem URLs para analisar.", file=sys.stderr)
        sys.exit(1)
    _site_check(urls)


def _site_check(urls): # Checa se cada URL está online e retorna uma mensagem com o resultado dessa checagem
    for url in urls:
        is_online, error = check_connection(url)
        display_check_result(url, is_online, error)


if __name__ == "__main__":
    main()
