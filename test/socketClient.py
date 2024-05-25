import mysql.connector

# MySQL 데이터베이스에 연결
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1017",
    database="rts"
)

# 쿼리 실행을 위한 커서 생성
cursor = mydb.cursor()

# 환자 ID
patient_id = 123  # 여기에 실제 환자의 ID를 넣어주세요

# 쿼리문 작성 (파라미터화)
query = """
SELECT patient.name, patient.address, guardian.guardianNumber
FROM patient
INNER JOIN guardian ON patient.id = guardian.id
WHERE patient.id = %s;
"""

# 쿼리 실행
cursor.execute(query, (patient_id,))

# 결과 가져오기
result = cursor.fetchone()

# 결과 출력
if result:
    name = result[0]
    address = result[1]
    guardian_number = result[2]
    print("이름:", name)
    print("주소:", address)
    print("보호자 전화번호:", guardian_number)
else:
    print("해당 환자 ID에 대한 정보를 찾을 수 없습니다.")

# 연결 종료
mydb.close()