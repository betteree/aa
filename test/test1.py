from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import queue

#받고 보내고
class StreamTCPsocket():
    def __init__(self,socket:socket,address):
        self.__socket=socket 
        self.__address=address

    def recv(self):
        data=self.__socket.recv()
        return data
    
    def send(self):
        data= self.__socket.send()
        return data
    


#string -> dict , dict ->string
class RealtimeServiceProtocol():
    def __init__(self,socket:socket,address):
        self.__socket=socket 
        self.__address=address
    
    # string data를 dict로 바꾸는 친구 
    def str_todict(self,data:str):
        list_data=data.split(" ") 
        dict_data = self.__method_checker(list_data[0])
        i = 1
        for k in dict_data.keys:
            dict_data[k] = list_data[i]
            i += 1

        return dict_data 
    
    def __method_checker(self, method):
        
        dict_data = {}
        #로그인
        if method == "Login":
            dict_data = {"method":"Login",
                         "ID" :"assd",
                         "PW" :"dsagdsag",
            }

        #gps데이터 전송
        elif method == "Gps":
            dict_data = {"method":"Gps",
                         "X" :"13.00",
                         "Y" :"14.00",
            }

        #회원가입
        elif method == "SignUp":
            dict_data ={"method":"SignUp",
                        "name":"김나은",
                        "guardNumber": "01030236298",
                        "patientNumber":"01011235677",
                        "address":"대구광역시",
                        "id":"adfadf",
                        "pw":"dafdsfa",

            }

        return dict_data

    # string data를 dict로 바꾸는 친구 
    def dict_tostr(self, data:dict):
        str_data = ""
        for value in data.values:
            str_data += value + " "

        return str_data    


#채팅방 - 환자와 보호자 짝찾아주는 클래스? 하나의 방 느낌
class ChattingRoom():

    def __init__(self, pid):
        self.__pid = pid
        self.__recv_que = queue.Queue()
        self.__send_que = queue.Queue()
        self.__client = []

    def input_client(self, client):
        self.__client.append()
        return 

    def set_pid(self, pid):
        self.__pid = pid

    def get_pid(self):
        return self.__pid
    
   #큐에 값 넣어주기 
    def is_queue_empty(self,):
        result = self.__send_que.empty()
        return result

    #큐에서 값 빼기
    def dequeue(self,):
        data = self.__recv_que.get()
        return data
   
    #큐에서 값 빼기
    def enqueue(self, data):
        self.__send_que.put(data)
        return

# 채팅룸을 관리하고 인터페이스를 제공하는 클래스
class ChattingRoomAPI:
    def __init__(self):
        self.chattingrooms = []  # 채팅룸 리스트

    #채팅룸 찾기
    def fineRoom(self, room_name):
        room = self.getroom(room_name) 
        if not room:
            room = self.createroom(room_name)
        return room

    #없으면 생성
    def createRoom(self, room_name):
        newroom = ChattingRoom(room_name)
        self.chattingrooms.append(new_room)
        return newroom
   
    #채팅룸 반환
    def getRoom(self, room_name):
        for room in self.chattingrooms:
            if room.get_pid() == room_name:
                return room
        return None

    #클라이언트 추가하기
    def addclientRoom(self, room_name, client):
        room = self.createroom(room_name)
        room.add_client(client)

    #비어있는지 확인하기
    def roomEmpty(self, room_name):
        room = self.findroom(room_name)
        return room.is_empty()
    


#로그인 및 회원가입 컨트롤러
class LoginController():

    #리스트 초기화 해주기
    def __init__(self):
        self.id_list = []
        self.pw_list = []
        self.name_list = []
        self.patient_number = []
        self.guardian_number = []
        self.address_list = []
        
    def signUp(self,data:dict):
        id_value = data.get('id')
        pw_value = data.get('pw')
        name_value = data.get('name')
        patient_number_value = data.get('patient_number')
        guardian_number_value = data.get('guardian_number')
        address_value = data.get('address')


    if id_value and pw_value and name_value and patient_number_value and guardian_number_value and address_value:
            self.id_list.append(id_value)
            self.pw_list.append(pw_value)
            self.name_list.append(name_value)
            self.patient_number.append(patient_number_value)
            self.guardian_number.append(guardian_number_value)
            self.address_list.append(address_value)
    else:
        print("값을 모두 입력 바람")                       
        
    
    def login(self, id_value, pw_value):
        if id_value in self.id_list:
            index = self.id_list.index(id_value)
            if self.pw_list[index] == pw_value:
                print("로그인 성공")
            else:
                print("로그인 실패")

        else:
            print("아이디없음")

#비동기서버 만드는 인터페이스
class RealTimeServiceASGI():

    def __init__(self,socket:socket,address):
        self.__socket=socket 
        self.__address=address 

    def socketServer(self):
        server_socket = socket.__socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind('localhost',9999)
        server_socket.listen()

        while True:
            client_socket, client_addr = server_socket.accept()
            try:
                data = client_socket.recv()
                if not data:
                    continue
                client_socket.send()
            finally:
                client_socket.close()

    #소켓끼리 데이터 송수신
    def recvThread(self,StreamTCPsocket,RealTimeServiceProtocol,ChattingRoom):
        while True:
            if not ChattingRoom.is_queue_empty():
                data = StreamTCPsocket.recv()
                dict_data = RealtimeServiceProtocol.str_todict(data)
                ChattingRoom.enqueqe(dict_data)
            else:
                print("큐에 데이터를 넣을 준비가 되지 않았습니다.")


    def sendThread():
        while True:
            if not ChattingRoom.is_queue_empty():
                data = ChattingRoom.dequeue()
                if data == True:
                    ChattingRoom.dequeqe(data)
                str_data = RealtimeServiceProtocol.dict_tostr(data)
                StreamTCPsocket.send(str_data)
            else:
                print("큐에 전송할 데이터가 없습니다.")
   

    def clientHandleThread(client_socket, client_address):
        server_socket = self.__socket_open(host=host, port=port)
        while True:
            client_socket, addr = server_socket.accept()
            client = self.__make_client(client_socket, addr)
            handler = Thread(target=func, args=(app, client, ))
            handler.start() 
            __client_socket.append(handler)
    