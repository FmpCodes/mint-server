# Using Python 3.xx
import socket


HOST, PORT = '', 8888


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

listen_socket.bind((HOST,PORT))

listen_socket.listen(1)


print(f'Serving HTTP on port {PORT} ...')

while True:
  client_connection, client_address = listen_socket.accept()
  request_data = client_connection.recv(1024)
  print(request_data.decode('utf-8'))

  http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
  client_connection.sendall(http_response)
  client_connection.close()

#Code Explanation

#Line 2 : The first line "import socket" is simply instructing the python interpreter to add or make visible the socket module of python which contains useful methods for executing an instance of a client<->server request-response cycle. 

#Line 4 : The values on the right are assigned the values on the left
