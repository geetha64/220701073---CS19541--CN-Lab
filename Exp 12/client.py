import socket
import time

def ping_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)  # Set a timeout of 5 seconds
        try:
            s.sendto(b'Hello', (host, port))
            data, addr = s.recvfrom(1024)
            print(f"Received reply from server: {data.decode()}")
        except socket.timeout:
            print("Request timed out")

if __name__ == "__main__":
    ping_server()
