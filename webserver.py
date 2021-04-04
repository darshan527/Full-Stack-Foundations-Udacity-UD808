from http import server
from http.server import BaseHTTPRequestHandler, HTTPServer
from helpers import *
from htmlHelpers import *


class WebServerHandler(BaseHTTPRequestHandler):
    def OKResponse(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
        print(message)

    def do_GET(self):
        if self.path.endswith("/restaurants"):
            message = getList(getRestaurant(), False)
            self.OKResponse(message=message)
            return

        elif self.path.endswith("/hello"):
            message = ""
            message += "<html><body>Hello World!</body></html>"
            self.OKResponse(message=message)
            return

        elif self.path.endswith("/add"):
            message = ""
            message += getForm()
            self.OKResponse(message=message)
            return
        else:
            self.send_error(404, "File Not Found: %s" % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(("", port), WebServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.shutdown()


if __name__ == "__main__":
    main()