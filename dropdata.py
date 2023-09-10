from mysql.connector import connect
conn=connect(
    host="localhost",
    user="root",
    password="root"
)
print("database Connected...")
sql="drop database employee"
curr= conn.cursor()
curr.execute(sql)
print("Database Drop...")
