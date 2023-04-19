from sitechecker.checker import check_connection


def test_connection():
    assert check_connection("indicium.tech") == True
    # assert check_connection("incidium.tech") == "[Errno 11001] getaddrinfo failed"
