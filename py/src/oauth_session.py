from requests_oauthlib import OAuth2Session
import http.server
from urllib.parse import urlparse, parse_qs
import threading
import webbrowser
import os
from dotenv import load_dotenv


class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    parsed_path = None

    def do_GET(self):
        self.__class__.parsed_path = urlparse(self.path)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"""
        <html>
            <body>
                <script>
                    alert("Authorized successfully. You can close this tab.");
                    window.open('', '_self', '');
                    window.close();
                </script>
            </body>
        </html>
        """)


def start_auth_server():
    httpd = http.server.HTTPServer(('0.0.0.0', 3456), HTTPRequestHandler)
    server_thread = threading.Thread(target=httpd.handle_request)
    server_thread.start()
    server_thread.join()


def fetch_code_and_close(redirect_response):
    params = parse_qs(redirect_response.query)
    code = params['code'][0]
    return code


def main():
    load_dotenv()

    client_id = os.getenv('GG_CLIENT_ID')
    redirect_uri = 'http://localhost:3456'
    authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    scope = ["https://www.googleapis.com/auth/drive"]

    google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = google.authorization_url(authorization_base_url,
                                                        access_type="offline",
                                                        include_granted_scopes="true",
                                                        state="state_parameter_passthrough_value")

    webbrowser.open(authorization_url)

    start_auth_server()

    redirect_response = HTTPRequestHandler.parsed_path
    code = fetch_code_and_close(redirect_response)
    print("Authorization code: ", code)


if __name__ == "__main__":
    main()
