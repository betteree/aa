from model import DB_API

# LoginController 클래스
class LoginController:
    def __init__(self):
        self.__dbAPI = DB_API()
    
    def try_login(self, raw_data:dict):
        
        id = raw_data['ID']
        pw = raw_data['PW']
        client_type = raw_data['TYPE']
        # result = {type, id, result}
        result = {}
        
        # 테스트용 코드
        result['id'] = id
        result['result'] = True
        result['type'] = client_type 
        
        return result
        # 테스트 끝
        
        if self.__dbAPI.check_id_exist(id):
            print("아이디 존재")
            if self.__dbAPI.verify_password(id, pw):
                print("로그인 성공")
                result['id'] = id
                result['result'] = True
                result['type'] = client_type 
            else:
                print("비밀번호가 올바르지 않습니다")
                result['result'] = False
        else:
            result['result'] = False
            print("아이디 존재하지 않음")
        return result
        
    
    def sign_up(self, id, pw, name, address, patientNumber, guardianNumber):
        newClient = ClientModel()
        newClient.set_id(id)
        newClient.set_pw(pw)
        newClient.set_name(name)
        newClient.set_address(address)
        newClient.set_patientNumber(patientNumber)
        newClient.set_guardianNumber(guardianNumber)
        newClient.set_pid(id)
        self.__DB.insert_client(newClient)