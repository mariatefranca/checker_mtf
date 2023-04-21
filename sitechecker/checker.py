from http.client import HTTPConnection
from urllib.parse import urlparse


def check_connection(url, timeout=2):
    """Retorna verdadeiro se a função estabelecer conexão com uma das portas HTTP ou HTTPS
    ou retorna falso e a mensagem de erro em caso de falaha na conexão."""
    # Defines a generic Exception as placeholder    # Parses URL and finds host
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    # Starts a for loop using HTTP and HTTPs ports
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True, ""
        except Exception as e:
            error = str(e)
        finally:
            connection.close()
    return False, error


