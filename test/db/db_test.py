"""
오라클 DB 연결 테스트

참고: https://almost-native.tistory.com/418 
"""
import oracledb

# DB 연결
oracledb.init_oracle_client()
con = oracledb.connect(user="scott", password="tiger", dsn="localhost:1521/xe")
cursor = con.cursor()
 
# Select 
# cursor.execute("select * from dept where deptno=10")
# out_data = cursor.fetchone()
# print("=====>", out_data[0])
# print("=====>", out_data[1])
# print("=====>", out_data[2])

# InsertMany
# cursor.executemany


con.close()