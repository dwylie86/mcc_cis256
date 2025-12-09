# David Wylie
# CIS256 24903
# EX8: Networking
# Simple Client Program for Exercise 8

import socket

ADDRESS = "localhost"  # "192.168.1.100" is my server addr
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ADDRESS, PORT))
    message = "Hello, Server"
    msg_bytes = message.encode()
    s.send(msg_bytes)
    data = s.recv(1024)
    print(f"Received: {data.decode()}")

# Common client connection errors
except ConnectionRefusedError:
    print(f"Error: Could not connect to {ADDRESS} server on port {PORT}")
except KeyboardInterrupt:
    print("\nClient interrupted")

finally:
    s.close()
