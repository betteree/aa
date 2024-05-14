import mysql.connector

# ClientModel 클래스
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

# DB_API 클래스
class DB_API:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1017",
            database='patient'
        )
        self.cursor = self.mydb.cursor()

    def insert_client(self, client):
        query = "INSERT INTO patient (id, pw, address, name, patient_number, guardian_number) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (
            client.get_id(),
            client.get_pw(),
            client.get_address(),
            client.get_name(),
            client.get_patientNumber(),
            client.get_guardianNumber()
        )
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("회원가입이 완료되었습니다.")

    def check_id_exist(self, id):
        query = "SELECT id FROM patient WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone() 

        if result:
            return True  
        else:
            return False  

    def verify_password(self, id, pw):
        query = "SELECT pw FROM patient WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()

        if result and result[0] == pw:
            return True
        else:
            return False

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

# LoginController 클래스
class LoginController:
    def __init__(self, DB):
        self.__DB = DB
    
    def try_login(self, id, pw):
        if self.__DB.check_id_exist(id):
            print("아이디 존재")
            if self.__DB.verify_password(id, pw):
                print("로그인 성공")
            else:
                print("비밀번호가 올바르지 않습니다")
        else:
            print("아이디 존재하지 않음")
    
    def sign_up(self, id, pw, name, address, patientNumber, guardianNumber):
        newClient = ClientModel()
        newClient.set_id(id)
        newClient.set_pw(pw)
        newClient.set_name(name)
        newClient.set_address(address)
        newClient.set_patientNumber(patientNumber)
        newClient.set_guardianNumber(guardianNumber)
        
        self.__DB.insert_client(newClient)

def main():
    # DB_API 객체 생성
    db_api = DB_API()
    
    # LoginController 객체 생성
    login_controller = LoginController(db_api)

    # 회원가입 정보 입력 받기
    print("회원가입을 시작합니다.")
    new_id = input("아이디를 입력하세요: ")
    new_pw = input("비밀번호를 입력하세요: ")
    new_name = input("이름을 입력하세요: ")
    new_address = input("주소를 입력하세요: ")
    new_patient_number = input("환자 번호를 입력하세요: ")
    new_guardian_number = input("보호자 번호를 입력하세요: ")

    # 회원가입 진행
    login_controller.sign_up(new_id, new_pw, new_name, new_address, new_patient_number, new_guardian_number)

    # 로그인 정보 입력 받기
    print("\n로그인을 시작합니다.")
    login_id = input("아이디를 입력하세요: ")
    login_pw = input("비밀번호를 입력하세요: ")

    # 로그인 시도
    login_controller.try_login(login_id, login_pw)

    # 데이터베이스 연결 종료
    db_api.close_connection()

if __name__ == "__main__":
    main()
