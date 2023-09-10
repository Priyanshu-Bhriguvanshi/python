from mysql.connector import connect
conn = connect(
    host= "localhost",
    user="root",
    password="root",
    database="employee"
)
print("database Connected...")
sql="update emp set ename='Sonali Singh' where eid=2"
curr=conn.cursor()
curr.execute(sql)
conn.commit()

