# David Wylie
# CIS256 24903
# EX8: Networking
# Simple Server Program for Exercise 8

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ADDRESS = "0.0.0.0"  # Accepts all connections, and localhost
PORT = 5555

# To avoid address in use error
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((ADDRESS, PORT))
server_socket.listen(5)
print(f"Server is listening on port {PORT}")

try:
    # While loop to stay open until ctrl+c
    while True:
        (client_socket, address) = server_socket.accept()
        print(f"Connected to {address}")

        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        message = "Hello, Client"
        msg_bytes = message.encode()
        client_socket.send(msg_bytes)
        client_socket.close()
        print(
            f"Connection with {address} closed. Awaiting next client...\n"
            "Press Ctrl + C to shut server down"
            )
except KeyboardInterrupt:
    print("\nServer shutting down, goodbye!")
finally:
    server_socket.close()
