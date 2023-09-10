from mysql.connector import connect
conn =connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
print("DataBase Connected...")
sql="truncate table emp"
curr=conn.cursor()
curr.execute(sql)
print("table truncate...")


