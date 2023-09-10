from mysql.connector import connect
conn = connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
print("Database Successfully Connected...")
sql="create table emp(eid int, ename varchar(20), dno int, sal int)"
curr= conn.cursor()
curr.execute(sql)
print("Table Created ...")
