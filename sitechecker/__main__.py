import sys

from sitechecker.checker import check_connection
from sitechecker.cli import read_user_cli_args, display_check_result


def main():
    """Run Site Checker."""
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("Erro: sem URLs para analisar.", file=sys.stderr)
        sys.exit(1)
    _site_check(urls)


def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = check_connection(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)


if __name__ == "__main__":
    main()
