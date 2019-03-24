import urllib.request
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from io import BytesIO
from time import sleep


class ImageHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_GET(self):
        response = urllib.request.urlopen('https://web-app.usc.edu/web/soc/api' + self.path)
        data = json.load(response)
        try:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        except BrokenPipeError: pass


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


from main import Threadable
class ThreadableMJPGSender(Threadable):
    def __init__(self):
        self.server = ThreadedHTTPServer(('localhost', 5000), ImageHandler)

    def run(self):
        ImageHandler.enabled = True
        self.server.serve_forever()

    def stop(self):
        ImageHandler.enabled = False
        self.server.shutdown()
