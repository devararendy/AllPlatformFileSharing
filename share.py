import pyqrcode
import sys
import socket
import argparse
import http.server
import socketserver

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't actually send data, just connects to find the local IP used for routing
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except Exception:
        # Fallback if the above fails (e.g., no network connection)
        IP = '127.0.0.1' 
    finally:
        s.close()
    return IP


ipaddr = get_local_ip()

parser = argparse.ArgumentParser("python ./qr.py")
parser.add_argument("port", help="port http server", type=int)
args = parser.parse_args()
port = args.port

data = "http://"+ipaddr+":"+str(port)

# Generate the QR code object
qr = pyqrcode.create(data)

# Print the QR code directly to the terminal
# The terminal() method uses ASCII characters for display
print(qr.terminal())


Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"serving at {data}")
    httpd.serve_forever()
