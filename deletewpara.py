from mysql.connector import connect
conn= connect(
    host='localhost',
    user='root',
    password="root",
    database="employee"
)
print("Database Connected...")
sql="delete from emp where eid=%s "
id=tuple(input("Enter id for row delete : "))
curr=conn.cursor()
curr.execute(sql,id)
conn.commit()
print(curr.rowcount, "Row Deleted...")
