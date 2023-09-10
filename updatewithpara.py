from mysql.connector import connect
#update with parameter
conn = connect(
    host= "localhost",
    user= "root",
    password= "root",
    database="employee"
)
print("database Connected...")
sql="update emp set ename=%s where eid=%s"
ename=input("Enter Emp name : ")
eid=int(input("Enter emp id : "))
val=(ename,eid)
curr=conn.cursor()
curr.execute(sql,val)
conn.commit()
print(curr.rowcount, "Row updated")
