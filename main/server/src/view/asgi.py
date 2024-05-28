from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
HOST = '172.20.10.3'
PORT = 9999

from view.RSP import RealtimeServiceProtocol
from view.socketTCPSocket import StreamTCPsocket
from controller import LoginController
from view.chatting_room_api import ChattingRoomAPI
from view.chatting_room import ChattingRoom

class RealTimeServiceASGI:
    def __init__(self):
        return

    def run_server(self):
        print("[ start server")
        self.__start_server()

    def __start_server(self):
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        print(f"ip : {HOST}  | port = {str(PORT)}")
        server_socket.listen()
    
        realtimeServiceProtocol = RealtimeServiceProtocol()
        chattingRoomAPI = ChattingRoomAPI()
        
        while True:
            client_socket, addr = server_socket.accept()
            streamTCPSocekt = StreamTCPsocket(socket=client_socket, address=addr,
                                            protocol=realtimeServiceProtocol)
            thread = Thread(target=self.clientHandleThread, args=(streamTCPSocekt, 
                                                                  chattingRoomAPI))
            thread.start()
        
        
    def clientHandleThread(self, streamTCPSocket:StreamTCPsocket,
                           chattingRoomAPI:ChattingRoomAPI):
        dict_data = streamTCPSocket.recv()
        # dict_data = {id, pw}
        login_controller = LoginController()
        user_data:dict = login_controller.try_login(dict_data)
        # user_data = {type, id, result}
        
        if not user_data['result']:
            # send() 하는데 님 실패했음 으로 알림
            return
        
        streamTCPSocket.set_user_type(user_type= user_data['type'])
        
        found_chatting_room = chattingRoomAPI.find_chatting_room(user_data['id'])
        found_chatting_room.queue_clear()
        recv_thread = Thread(target=self.__recvThread,
                             args=(streamTCPSocket, found_chatting_room))
        send_thread = Thread(target=self.__sendThread,
                             args=(streamTCPSocket, found_chatting_room))
        
        recv_thread.start()
        send_thread.start()
        
        recv_thread.join()
        send_thread.join()
        return
    
        
    def __recvThread(self, streamTCPSocket:StreamTCPsocket,
                     chatting_room:ChattingRoom):
        user = streamTCPSocket.get_user_type()
        while True:
            dict_data = streamTCPSocket.recv()
            #print('recv_thread dict_data : ', dict_data)
            if user == 'gardian':
                chatting_room.recv_gardian_enque(dict_data)
            elif user == 'patient':
                chatting_room.recv_patient_enque(dict_data)
                chatting_room.send_gardian_enque(dict_data)
        return

    def __sendThread(self, streamTCPSocket:StreamTCPsocket,
                     chatting_room:ChattingRoom):
        user = streamTCPSocket.get_user_type()
        print(f"user : {user}",chatting_room)
        while True:
            result = True
            dict_data = None
            
            if user == "gardian":
                result = chatting_room.is_gardian_sendque_empty()
                if not result:
                    dict_data = chatting_room.send_gardian_deque()
                    print(dict_data)
                    
            elif user == "patient":
                result = chatting_room.is_patient_sendque_empty()
                if not result:
                    dict_data = chatting_room.send_patient_deque()
                
            if not result:
                streamTCPSocket.send(dict_data)
                dict_data = None
            
        return