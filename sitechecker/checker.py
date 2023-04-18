from http.client import HTTPConnection
from urllib.parse import urlparse


def check_connection(url, timeout=2):
    """Return True if the target URL is online.

    Raise an exception otherwise.
    """
    # Defines a generic Exception as placeholder
    error = Exception("Ops, algo errado.")
    # Parses URL and finds host
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    # Starts a for loop using HTTP and HTTPs ports
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error


def test_connection():
    assert connection_checker("indicium.tech") == True
