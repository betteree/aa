
class Client_Model():
    def __init__(self):
        self.__id = 0
        self.__pw = "default"

    def set_id(self, id):
        self.__id = id
        return

    def set_pw(self, pw):
        self.__pw = pw
        return

    def get_id(self):
        return self.__id

    def get_pw(self):
        return self.__pw

class Fake_DB_API():
    def __init__(self):
        self.__client_list = []
        my_sql_pt


    def add_client(self, id, pw):
        client = Client_Model()
        client.set_id(id)
        client.set_pw(pw)
        self.__client_list.append(client)
        return

    def find_client_with_id(self, id):
        client_list = my_sql_pt.query("select client from ")
        for client in client_list:
            find_id = client.get_id()
            if id == find_id:
                return True
        return False



class Login():
    def __init__(self, db):
        self.__db = db
        return

    def try_login(self, id, pw):
        new_client= Client_Model()
        new_client.set_id(id)
        new_client.set_pw(pw)
        if self.__db.find_client_with_id(id=new_client.get_id()):
            print("true")
        else:
            print("false")

        
import time
from threading import Thread

class Flag:
    def __init__(self):
        self.__flag = False
        self.__date = 0

    def get_flag(self):
        self.__new_date()
        return self.__flag

    def __new_date(self):
        if self.__date == 1:
            self.__date = 0
        else:
            self.__date = 1
        print(self.__date)
        return

    def set_flag(self, flag):
        self.__new_date()
        self.__flag = flag
        return


def func1(flag):
    print(flag)
    i = 0
    while True:
        if flag.get_flag():
            break
        time.sleep(0.5)
        print("hello")

    return


if __name__ == "__main__":
    #db = Fake_DB()
    #db.add_client(id='qwer', pw='qwer')

    #login = Login(db)
    #login.try_login(id='rewq', pw='qwer')

    flag = Flag()

    
    thread = Thread(target=func1, args=(flag,))
    thread.start()

    i = 0
    print(flag)
    while True:
        if i == 5:
            break
        time.sleep(1)
        print("qwer")
        i += 1
    flag.set_flag(True)

    thread.join()



