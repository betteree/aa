import mysql.connector


# DB_API 클래스
class DB_API:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1017",
            database='rts'
        )
        self.cursor = self.mydb.cursor()


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
        
    def save_gps_data(self, load_name):
        query = "INSERT INTO location (repeated_Location) VALUES (%s)"
        values = (
            load_name,
         )
        self.cursor.execute(query, values)
        self.mydb.commit()
        
        # # 1. location 테이블에 해당 장소가 있는지 확인합니다.
        # select_query = "SELECT id_Location FROM location WHERE repeated_Location = %s"
        # self.cursor.execute(select_query, (load_name,))
        # location_data = self.cursor.fetchone()

        # if location_data:  # 장소가 이미 있는 경우
        #     location_id = location_data[0]

        #     # 2. visit 테이블에 해당 장소와 환자가 있는지 확인합니다.
        #     select_visit_query = "SELECT counting FROM visit WHERE id_Location = %s AND id_Patient = %s"
        #     self.cursor.execute(select_visit_query, (location_id, id_patient))
        #     visit_data = self.cursor.fetchone()

        #     if visit_data:  # 장소와 환자가 있는 경우
        #         # 해당 장소와 환자의 counting을 증가시킵니다.
        #         update_visit_query = "UPDATE visit SET counting = counting + 1 WHERE id_Location = %s AND id_Patient = %s"
        #         self.cursor.execute(update_visit_query, (location_id, id_patient))
        #         print("Visit count updated.")
        #     else:  # 장소와 환자가 없는 경우
        #         # visit 테이블에 새로운 행을 추가합니다.
        #         insert_visit_query = "INSERT INTO visit (id_Patient, id_Location, counting) VALUES (%s, %s, 1)"
        #         self.cursor.execute(insert_visit_query, (id_patient, location_id))
        #         print("New visit entry added.")
        # else:  # 장소가 없는 경우
        #     # 3. location 테이블에 장소를 추가합니다.
        #     insert_location_query = "INSERT INTO location (repeated_Location) VALUES (%s)"
        #     self.cursor.execute(insert_location_query, (load_name,))
        #     self.mydb.commit()

        #     # 삽입된 위치의 id_Location 값을 가져옵니다.
        #     get_location_id_query = "SELECT id_Location FROM location WHERE repeated_Location = %s"
        #     self.cursor.execute(get_location_id_query, (load_name,))
        #     location_id = self.cursor.fetchone()[0]

        #     # 4. visit 테이블에 새로운 행을 추가합니다.
        #     insert_visit_query = "INSERT INTO visit (id_Patient, id_Location, counting) VALUES (%s, %s, 1)"
        #     self.cursor.execute(insert_visit_query, (id_patient, location_id))
        #     print("New location and visit entry added.")

        # # 변경 사항을 커밋합니다.
        # self.mydb.commit()


    
    def get_gps_data(self,):
        query = """
        SELECT location
        FROM visit
        ORDER BY counting DESC
        LIMIT 3 OFFSET 3;
        """
        
        cursor.execute(query)
        predict_location = cursor.fetchall()
        
        return predict_location
          
    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

    # def insert_client(self, client):
    #     query = "INSERT INTO patient (id, pw, address, name, patient_number, guardian_number) VALUES (%s, %s, %s, %s, %s, %s)"
    #     values = (
    #         client.get_id(),
    #         client.get_pw(),
    #         client.get_address(),
    #         client.get_name(),
    #         client.get_patientNumber(),
    #         client.get_guardianNumber()
    #     )
    #     self.cursor.execute(query, values)
    #     self.mydb.commit()
    #     print("회원가입이 완료되었습니다.")