from http.server import SimpleHTTPRequestHandler
import socketserver
import webbrowser
import threading


class ChartServer:
    def __init__(self, port=8000):
        self.port = port
        self.server = None
        self.thread = None

    def start(self):
        # Set up the server in a new thread
        Handler = SimpleHTTPRequestHandler
        self.server = socketserver.TCPServer(("", self.port), Handler)
        self.thread = threading.Thread(target=self._run_server)
        self.thread.start()
        print(f"Server started at port {self.port}")

    def _run_server(self):
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass  # Allow for clean shutdown on keyboard interrupt

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
        if self.thread and self.thread.is_alive():
            self.thread.join()
        print("Server stopped.")

    def open_chart(self, chart, filename='index.html'):
        chart.save(filename)
        webbrowser.open(f'http://localhost:{self.port}/{filename}')
