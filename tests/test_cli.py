from sitechecker.cli import read_user_cli_args, generate_check_results


def test_read_user_cli_args() -> None:
    args = read_user_cli_args(["-u", "google.com", "terraa.com"])
    assert args.urls == ["google.com", "terraa.com"]

def test_generate_check_results():
    assert generate_check_results(True, "indicium.tech") == 'O status da "indicium.tech" é: "Online!"'
    assert generate_check_results(False, "incidium.tech") == 'O status da "incidium.tech" é: "Offline?"\n  Erro: ""'


