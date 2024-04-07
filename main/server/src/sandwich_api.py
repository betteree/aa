from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

HOST = "127.0.0.1"
PORT = 5000

class SandwichAPI():
    def __init__(self):
        # TCP 소켓 만들기
        self.__client_routes = []
        self.__clients = []
        self.__server_socket = socket(AF_INET, SOCK_STREAM)

    def run_server(self):
        self.__server_socket.bind((HOST, PORT))
        self.__server_socket.listen()


    def waiting_client(self):
        while True:
            client_socket, addr = self.__server_socket.accept()
            print(f"New Client accepted : {addr}")
            client_thread = Thread(target=self.client_handler,
            args=(client_socket,))
            self.__clients.append(client_thread)
            client_thread.start()
                
    def client_handler(self, client_socket):
        connect_data = client_socket.recv()
        cp = ConnectionParser()
        method = cp.data_parsing(connect_data)

        # 메서드가 틀렸다면? 소켓 닫아버리기
        if method != "login":
            client_socket.send("bad request")
            return

        id, pw = cp.get_id_n_pw()

        # 로그인 시도
        ic = InitController()
        result:bool = ic.try_login(id, pw)

        # 로그인 실패시 소켓 닫아버리기
        if not result:
            client_socket.send("wrong id and pw")
            return
        
        user_type, gardian, patient = ic.get_login_info()

        flag = False

        client_route = None

        #내자리 찾기
        for client in self.__client_routes:
            if user_type == "gardian":
                gid = client.get_gardian_ID()
                if gid == gardian.get_gid():
                    flag = True
                    client_route = client
            elif user_type == "patient":
                pid = client.get_patient_ID()
                if pid == patient.get_pid():
                    flag = True
                    client_route = client
        
        # 찾았니?
        if not flag:
            client_route = ClientRoute(
                gardian=gardian, patient=patient)
            self.__client_routes.append(client_route)

        send_thread = Thread(
            target=self.__socket_send, args=(
                user_type,client_socket, client_route ))
        recv_thread = Thread(
            target=self.__socket_recv, args=(
                user_type,client_socket, client_route ))
        send_thread.start()
        recv_thread.start()

    #data = "method from body"

    def __socket_send(self, user_type, client_socket, client_route):
        parser = SendParser()
        while True:
            if user_type == "gardian":
                flag = client_route.get_patient_flag()
            elif user_type == "patient":
                flag = client_route.get_gardian_flag()

            if flag:
                result = client_route.get_send_data()
                result = parser.parsing(parser)
                client_socket.send(result)
                if user_type == "patient":
                    flag = client_route.set_gardian_flag(False)
                elif user_type == "gardian":
                    flag = client_route.get_patient_flag(False)

    def __socket_recv(self, user_type, client_socket, client_route):
        parser = ReciveParser()
        while True:
            raw_data = client_socket.recv()

            method, body = parser.parsing(raw_data)

            result:bool = client_route.search_route(method, body)

            if not result:
                continue

            if user_type == "gardian":
                flag = client_route.set_gardian_flag(True)
            elif user_type == "patient":
                flag = client_route.get_patient_flag(True)








