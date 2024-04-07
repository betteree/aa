import TcpServer
import JsonParser
from controller import UserController, AlarmController, LocationController


class PatientView:
    def __init__(self, data):
        self.__data = data
        pass

    # request = ""
    def run(self):
        pass

class GuardianView:
    def __init__(self, data):
        self.__data = data
        pass
    
    # request = "login, sign_up, location, alarm, user_info"
    def run(self):
        requset = self.__data["header"]["request"]
        body = self.__data['body']
        result = self.__checkRequest(requset, body)
        return result

    def __checkRequest(self, requset, body):
        if requset == "login":
            result = self.__tryLogin(body)
        elif requset == "sign_up":
            result = self.__trySignUP(body)
        elif requset =="location":
            result = self.__tryLocation(body)
        elif requset =="alarm":
            result = self.__tryalarm(body)
        elif requset =="user_info":
            result = self.__tryUserInfo(body)
        else:
            return "badrequest"
    
        return result

    def __tryLogin(self, body):
        userController = UserController(body)
        result = userController.tryLogin()
        return result
    
    def __trySignUP(self, body):
        userController = UserController(body)
        result = userController.trySignUp()
        return result

    def __tryLocation(self, body):
        locationController =LocationController(body)
        result = locationController.tryLocation()
        return result

    def __tryalarm(self, body):
        alarmController = AlarmController(body)
        result = alarmController.tryalarm()
        return result
                                        
    def __tryUserInfo(self, body):
        userController = UserController(body)
        result = userController.tryInfo()
        return result



        
class ManagerView:
    def __init__(self) -> None:
        pass



class View:
    def __init__(self):
        self.__app=TcpServer() #app 무한루프 도는 중 recieve 기다리는 중
        self.__jsonParser=JsonParser()

    def route(self):
        while(True):
            try:
                result = None
                if self.__app.getFlag():
                    data= self.__app.getData()
                    parsedData=self.__jsonParser.excuteParsing(data)
                    usertype=parsedData["header"]["usertype"]
                    if usertype == "patient":
                        result=self.__guardView(parsedData)
                    elif usertype == "guardian":
                        result=self.__patientView(parsedData)
                    elif usertype =="manager":
                        result=self.__managerView(parsedData)
                    else:
                        result="badRequest"

                    returnData  = self.__jsonParser.setJsonData(result)
                    self.__app.setSendData(returnData)
                    result = None
                else:
                    continue
            except Exception as e:
                print(e)

    def __guardView(self,data):
        patientView=PatientView(data)
        result=patientView.run()
        return result
    
    def __patientView(self,data):
        patientView=PatientView(data)
        result=patientView.run()     
        return result
    
    def __managerView(self,data):
        patientView=PatientView(data)
        result=patientView.run()      
        return result

    def runServer(self):  #app가 무한이 돈다했으니 그게 돌아가는 함수
        pass

