#coding:utf-8

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urllib
from CS_match import CS_Match
from config import ChatScriptSercer, localServer


class TestHTTPHandle(BaseHTTPRequestHandler):


    def do_GET(self):
        m = CS_Match(ChatScriptSercer["host"], ChatScriptSercer["port"], ChatScriptSercer["timeout"])

        requestline = self.requestline

        buf = requestline.replace("GET /", "")
        buf = buf.replace(" HTTP/1.1", "")

        self.protocal_version = "HTTP / 1.1"
        self.send_response(200)
        self.send_header("Welcome", "Contect")
        self.end_headers()


        buf = buf.encode("utf8")

        response = urllib.unquote(buf)
        response = m.match(response)   #在这里调用ChatScript

        print "response: " + response

        self.wfile.write(str(response))


def start_server(host,port):
    http_server = HTTPServer((host, int(port)), TestHTTPHandle)
    http_server.serve_forever()

if __name__ == '__main__':
    start_server(localServer["host"], localServer["port"])