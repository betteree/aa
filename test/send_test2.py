from socket import socket, AF_INET, SOCK_STREAM

def main():
    HOST = "127.0.0.1"
    PORT = 9999
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    message = "x:165 y:98"
    message = message.encode()

    client_socket.send(message)

    #print(len(head))

    #print(length)

    result = client_socket.recv(1024).decode()
    print(result)

if __name__ == "__main__":
    main()