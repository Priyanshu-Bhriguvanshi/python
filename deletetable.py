from mysql.connector import connect
conn = connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
print("database Connected...")
sql="delete from emp where eid =2"
curr=conn.cursor()
curr.execute(sql)
print("Row delete")
conn.commit()
