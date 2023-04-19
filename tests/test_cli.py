from sitechecker.cli import read_user_cli_args, generate_check_results


def test_read_user_cli_args() -> None:
    args = read_user_cli_args(["-u", "google.com", "terraa.com"])
    assert args.urls == ["google.com", "terraa.com"]


def test_generate_check_results():
    assert generate_check_results("indicium.tech", True, "") == 'O status da "indicium.tech" é: "Online!"'
    assert generate_check_results(
        "incidium.tech", False, "[Errno 11001] getaddrinfo failed"
    ) == 'O status da "incidium.tech" é: "Offline?"\n  Erro: "[Errno 11001] getaddrinfo failed"'
