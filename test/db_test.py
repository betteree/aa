import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="1017",
    db='patient'
)

# 데이터베이스 커서 생성
cursor = mydb.cursor()

try:
    # patient 테이블에서 모든 정보 조회
    sql = "SELECT * FROM patient"
    
    # 쿼리 실행
    cursor.execute(sql)
    
    # 쿼리 결과 가져오기
    result = cursor.fetchall()
    
    # 결과 출력
    for row in result:
        print(row)  # 각 환자 정보 출력 (튜플 형태)
        
except Exception as e:
    print(f"Error: {e}")

finally:
    # 커서와 데이터베이스 연결 닫기
    cursor.close()
    mydb.close()
