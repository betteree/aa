class ChatRoom:
    def __init__(self, pid):
        self.clients = []
        self.pid = pid

    def input_client(self, client):
        self.clients.append(client)

    def set_pid(self, pid):
        self.pid = pid

class ChatApplication:
    def __init__(self):
        self.chattingrooms = []

    # 채팅룸 찾기
    def find_room(self, room_name):
        for room in self.chattingrooms:
            if room.name == room_name:
                return room
        return None

    # 클라이언트 추가하기
    def add_client_room(self, room_name, client):
        chattingRoom = self.find_room(room_name)
        if not chattingRoom:
            chattingRoom = self.create_room(room_name)
        
        chattingRoom.input_client(client)
        return chattingRoom

    # 채팅룸 생성하기
    def create_room(self, room_name):
        chattingRoom = ChatRoom(room_name)
        chattingRoom.set_pid(room_name + "_id")  # Set PID to some value
        self.chattingrooms.append(chattingRoom)
        return chattingRoom

# 사용 예시
app = ChatApplication()
new_room = app.create_room("General")
print(f"PID:{new_room.pid}")


new_room1 = app.create_room("aa")
print(f"PID: {new_room1.pid}")

# 다른 곳에서 PID를 사용
print(f"Using the room's PID: {new_room.pid}")
print(f"Using the room's PID: {new_room1.pid}")