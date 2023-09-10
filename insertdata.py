from mysql.connector import connect
conn= connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
print("Database Successfully Connected...")
sql="insert into emp values(2, 'Golden', 102, 30000, 'singhpriyanshu144@gmail.com')"
curr= conn.cursor()
curr.execute(sql)
print("value Inserted into emp...")
conn.commit()

