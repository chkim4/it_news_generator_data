"""
오라클 DB 연결 테스트

참고: https://almost-native.tistory.com/418 
"""
import oracledb

# Connect DB
oracledb.init_oracle_client()
con = oracledb.connect(user="scott", password="tiger", dsn="localhost:1521/xe")
cursor = con.cursor()

# Create Test Table 

# Insert (Write to DB)
# create table TEST_TBL ( aa varchar2(100) );
# in_data = "Hello World"
# cursor.execute("insert into TEST_TBL (aa) values (:1)", [in_data])
# con.commit()
 
# Select (Read from DB)
cursor.execute("select * from dept where deptno=10")
out_data = cursor.fetchone()
print("=====>", out_data[0])
print("=====>", out_data[1])
print("=====>", out_data[2])
 
con.close()