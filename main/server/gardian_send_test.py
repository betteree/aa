import time
from threading import Thread

from socket import socket, AF_INET, SOCK_STREAM
def main():

    HOST = "127.0.0.1"
    PORT = 9999
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    request = "Login qwer qwer gardian"
    request = request.encode()
    client_socket.sendall(request)
    
    time.sleep(1)
    
    flag = [True]
    send_thread = Thread(target=send, args=(client_socket,flag, ))
    recv_thread = Thread(target=recv, args=(client_socket,flag, ))

    send_thread.start()
    recv_thread.start()

    send_thread.join()
    recv_thread.join()

def send(client_socket:socket, flag):
    while flag[0]:
        time.sleep(1)
        

def recv(client_socket:socket, flag):
    while flag[0]:
        time.sleep(0.5)
        recv_data = client_socket.recv(1024)
        print(recv_data.decode())


if __name__ == "__main__":
    main()