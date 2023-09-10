from mysql.connector import connect
conn= connect(
    host='localhost',
    user="root",
    password="root"
)
print("Database Connected...")
sql="create database employee"
curr=conn.cursor()
curr.execute(sql)
print("Database Created...")
