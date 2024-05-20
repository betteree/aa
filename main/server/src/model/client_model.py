

#클라이언트 모델
class ClientModel:
    def __init__(self):
        self.__id = ""
        self.__pw = ""
        self.__address = ""
        self.__name = ""
        self.__patientNumber = ""
        self.__guardianNumber = ""
    
    def set_id(self, id):
        self.__id = id
    
    def set_pw(self, pw):
        self.__pw = pw
    
    def set_address(self, address):
        self.__address = address
    
    def set_name(self, name):
        self.__name = name

    def set_patientNumber(self, patientNumber):
        self.__patientNumber = patientNumber

    def set_guardianNumber(self, guardianNumber):
        self.__guardianNumber = guardianNumber

    def get_id(self):
        return self.__id

    def get_pw(self):
        return self.__pw

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_patientNumber(self):
        return self.__patientNumber

    def get_guardianNumber(self):
        return self.__guardianNumber



