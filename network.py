# import socket
# import threading

from icecream import ic

# def handle_client(client_socket):
#     try:
#         data = client_socket.recv(1024).decode()
#         ic(f"Received from client: {data}")
#         client_socket.sendall("Hey client".encode())
#     except Exception as e:
#         ic(f"Exception: {e}")
#     finally:
#         client_socket.close()
    
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ("localhost", 8095)
# server_socket.bind(server_address)
# server_socket.listen(5)

# ic("Server listening on: ", server_address)

# while True:
#     client_socket, client_address = server_socket.accept()
#     ic("Connected by: ", client_address)
#     client_handler = threading.Thread(target=handle_client, args=(client_socket,))
#     client_handler.start()

import requests

url = "https://news.ycombinator.com"

res = requests.get(url)

ic("Response code: ", res.status_code)
ic(res.text)