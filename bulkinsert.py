from mysql.connector import connect
#bulk insert
conn = connect(host= "localhost", user= "root", password= "root", database="employee")
print("database Connected...")
sql="insert into emp value(%s, %s, %s, %s, %s)"
list=[]
while True:
    eid = int(input("Enter emp id : "))
    ename =input("Enter emp name : ")
    dno=int(input("Enter dno : "))
    sal = int(input("Enter emp Salary : "))
    email=input("Enter Email : ")
    val=(eid,ename,dno,sal,email)
    list.append(val)
    choice=input("do You Want to continue  ? Y or N").lower()
    if choice == "n":
        break
curr=conn.cursor()
curr.executemany(sql,list)
print(curr.rowcount,"Record Inserted")
conn.commit()
