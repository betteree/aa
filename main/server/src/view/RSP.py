
#string -> dict , dict ->string
class RealtimeServiceProtocol:
    def __init__(self):
        return
    
    # string data를 dict로 바꾸는 친구 
    def str_to_dict(self,data:str):
        list_data=data.split(" ") 
        dict_data = self.__method_checker(list_data[0])
        i = 0
        for k in dict_data.keys():
            dict_data[k] = list_data[i]
            i += 1

        print('dict_data :', dict_data)
        return dict_data 
    
    def __method_checker(self, method):
        
        dict_data = {}
        #로그인
        if method == "Login":
            dict_data = {"method":"Login",
                         "ID" :"assd",
                         "PW" :"dsagdsag",
                         "TYPE":"default"
            }

        #gps 데이터 전송
        elif method == "GPS":
            dict_data = {"method":"GPS",
                         "X" :"13.00",
                         "Y" :"14.00",
            }

        return dict_data

    # string data를 dict로 바꾸는 친구 
    def dict_to_str(self, data:dict):
        str_data = ""
        for value in data.values():
            str_data += value + " "

        return str_data    
