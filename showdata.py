from mysql.connector import connect
conn = connect(
    host="localhost",
    user="root",
    password="root"
)
print("Database Successfully connected...")
sql = "show databases"
curr = conn.cursor()
curr.execute(sql)
for dbname in curr:
    print(dbname)
