from socket import socket 
import queue


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
    

class Realtime_serviceProtocol():
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
            dict_data = {"method":"",
                         "ID" :"",
                         "PW" :"",
            }

        #gps데이터 전송
        elif method == "Gps":
            dict_data = {"method":"",
                         "X" :"",
                         "Y" :"",
            }

        #회원가입
        elif method == "SignUp":
            dict_data ={"method":"",
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


class Chatting_room():

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



class LoginController():


    def sign_up(self,id,):

    def login():
    