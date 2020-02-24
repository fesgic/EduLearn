import connection
my_username = input("Username:")
client_socket = connection.socket.socket(connection.socket.AF_INET, connection.socket.SOCK_STREAM)
client_socket.connect((connection.IP, connection.PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{connection.HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f"{my_username} > ")

    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{connection.HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        while True:
            #receive things
            username_header = client_socket.recv(connection.HEADER_LENGTH)
            if not len(username_header):
                print("connection closed by server")
                connection.sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(connection.HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(username_length).decode('utf-8')

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != connection.errno.EAGAIN or e.errno != connection.errno.EWOULDBLOCK:
            print('Reading error', str(e))
            connection.sys.exit()

    except Exception as e:
        print('General error',str(e))
        connection.sys.exit()
