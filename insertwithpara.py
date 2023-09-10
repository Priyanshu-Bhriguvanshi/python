from mysql.connector import connect
#insert command with parameter
conn = connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
print("Database Connected...")
sql="insert into emp values(%s, %s,%s,%s,%s)"
eid=int(input("Enter employee id : "))
ename=input("Enter Employee Name : ")
dno=int(input("Enter Employee Dno. : "))
email=input("Enter Emnail : ")
sal=int(input("Enter salary : "))
val= (eid, ename, dno, sal,email )
curr=conn.cursor()
curr.execute(sql, val)
conn.commit()
