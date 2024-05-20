from socket import socket

#받고 보내고
class StreamTCPsocket():
    def __init__(self,socket:socket,address, protocol):
        self.__socket=socket 
        self.__address=address
        self.__realtimeServiceProtocol = protocol
        self.__user_type = None

    def recv(self):
        data=self.__socket.recv(1024).decode()
        dict_data = self.__realtimeServiceProtocol.str_to_dict(data)
        return dict_data
    
    def send(self, send_data):
        str_data:str = self.__realtimeServiceProtocol.dict_to_str(send_data)
        self.__socket.send(str_data.encode())
        return
    
    def set_user_type(self, user_type):
        self.__user_type = user_type
        return
    
    def get_user_type(self,):
        return self.__user_type
        