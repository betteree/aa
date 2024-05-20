import mysql.connector


# DB_API 클래스
class DB_API:
    def __init__(self):
        pass
        #self.mydb = mysql.connector.connect(
            #host="localhost",
            #user="root",
            #password="1017",
            #database='patient'
        #)
        #self.cursor = self.mydb.cursor()

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

    def __verify_password(self, id, pw):
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
