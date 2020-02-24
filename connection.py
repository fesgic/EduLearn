import socket
import select
import errno

HEADER_LENGTH = 100

IP=socket.gethostbyname(socket.gethostname())
PORT = 1234
