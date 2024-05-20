from view.chatting_room import ChattingRoom


# 채팅룸을 관리하고 인터페이스를 제공하는 클래스
class ChattingRoomAPI:
    def __init__(self):
        self.__chatting_room_list = []  # 채팅룸 리스트
        
    def find_chatting_room(self, room_name):
        found_chatting_room = self.__find_room(room_name=room_name)
        
        # 못찾음
        if not found_chatting_room:
            found_chatting_room = self.__create_room(room_name=room_name)
            
        return found_chatting_room
    

    #채팅룸 찾기
    def __find_room(self, room_name):
        found_room = None
        for room in self.__chatting_room_list:
            if room.get_room_name() == room_name:
                found_room = room
        return found_room
    
    #채팅룸이 없으면 생성하기 
    def __create_room(self, room_name):
        chattingRoom =ChattingRoom(room_name)
        self.__chatting_room_list.append(chattingRoom)
        return chattingRoom
