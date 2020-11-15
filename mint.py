# Using Python 3.xx
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

listen_socket.bind((HOST,PORT))

listen_socket.listen(1)
