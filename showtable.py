from mysql.connector import connect
conn = connect(
    host='localhost',
    user="root",
    password="root",
    database="employee"
)
print("Database Connected...")
sql="show tables"
curr=conn.cursor()
curr.execute(sql)
for table in curr:
    print(table)
