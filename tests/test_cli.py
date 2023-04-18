from sitechecker.cli import read_user_cli_args

def test_read_user_cli_args() -> None:
    args = read_user_cli_args(["-u", "google.com", "terraa.com"])
    assert args.urls == ["google.com", "terraa.com"]

