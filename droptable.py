from mysql.connector import connect
conn= connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
print("Database Connected Successfully...")
sql="drop table emp"
curr=conn.cursor()
curr.execute(sql)
print("Table Drop Successfully...")
