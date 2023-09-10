from mysql.connector import connect
conn = connect(
    host = 'localhost',
    user= 'root',
    password = 'root',
    database = 'employee'
)
print("database Connected ...")
sql= "alter table emp add email varchar(30)"
curr= conn.cursor()
curr.execute(sql)
print("Table Altered")
