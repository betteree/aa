from queue import Queue
from threading import Thread
from controller import PredictPlaceLogic
from controller import GPSSaveLogic


#채팅방 - 환자와 보호자 짝찾아주는 클래스? 하나의 방 느낌        
class ChattingRoom():
    def __init__(self, name):
        self.__gps_save_logic = GPSSaveLogic()
        self.__recv_gardian_que = Queue()
        self.__recv_patient_que = Queue()
        self.__send_patient_que = Queue()
        self.__send_gardian_que = Queue()
        self.__chatting_room_name:str = name
        thread = Thread(target=self.__controller_api_thread)
        thread.start()
        
    def get_room_name(self):
        return self.__chatting_room_name
        
    def __controller_api_thread(self):
        while True:
            result = True
            result = self.__is_gardian_recvque_empty()
            if not result:
                dict_data = self.__recv_gardian_deque()
                predict_place_logic = PredictPlaceLogic()
                logic_data = predict_place_logic.predict()
                self.send_gardian_enque(logic_data)
                
            result = True
            result = self.__is_patient_recvque_empty()
            if not result:
                dict_data = self.__recv_patient_deque()
                self.__gps_save_logic.is_save_GPS(dict_data)
        return

    def recv_gardian_enque(self, data):
        self.__recv_gardian_que.put(data)
        return
    
    def send_gardian_enque(self, data):
        self.__send_gardian_que.put(data)
        return
    
    def recv_patient_enque(self, data):
        self.__recv_patient_que.put(data)
        return
    
    
    def is_gardian_sendque_empty(self)->bool:
        result = self.__send_gardian_que.empty()
        return result
    
    def __is_gardian_recvque_empty(self)->bool:
        result = self.__recv_gardian_que.empty()
        return result
        
    def send_gardian_deque(self):
        dict_data = self.__send_gardian_que.get()
        return dict_data
    
    def __recv_gardian_deque(self):
        dict_data = self.__recv_gardian_que.get()
        return dict_data
        
    def is_patient_sendque_empty(self)->bool:
        result = self.__send_patient_que.empty()
        return result
    
    def __is_patient_recvque_empty(self)->bool:
        result = self.__recv_patient_que.empty()
        return result
        
    def send_patient_deque(self):
        dict_data = self.__send_patient_que.get()
        return dict_data
        
    def __recv_patient_deque(self):
        dict_data = self.__recv_patient_que.get()
        return dict_data
        
        
