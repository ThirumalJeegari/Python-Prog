
import mysql.connector

dbC = mysql.connector.connect(
host = "localhost",
user = "root",
password = "Thirumal@2004",
database = "thirumal"
)

# print(dbC,"10th Line")

print("db Connected Successfully...")

TableCreationQuery = """
create table if not exists employees(
    id int primary key,
    name varchar(50) not null,
    email varchar(50) not null unique,
    age int,
    salary decimal(10,2) not null
)
"""


cur = dbC.cursor()
cur.execute(TableCreationQuery)
# print("Table Created Successfully...")

print()
while True:
    print("1.ADD Employees Details")
    print("2.READ Employees Details")
    print("3.UPDATE Employees Details")
    print("4.DELETE Employees Details")
    print("5.EXIT")

    o = int(input("Enter your choice here :"))

    print()

    if o == 1:
        i = int(input("Enter Employee ID :"))
        n = input("Enter Employee Name :")
        e = input("Enter Employee Email :")
        a = int(input("Enter Employee age :"))
        s = float(input("Enter Employee salary :"))
        InsertTableValues = "insert into employees(id,name,email,age,salary)values(%s,%s,%s,%s,%s)"
        data = (i,n,e,a,s)
        cur.execute(InsertTableValues,data)
        dbC.commit()
        print("Employees Details ADD Successfully...")

    elif o == 2:
        ReadingTableValues = "select * from employees"
        cur.execute(ReadingTableValues)
        data = cur.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])
        print()

    elif o == 3:
        print()
        UpdatingTableValues = "update employees set salary = %s where id = %s"
        print()

        ReadingTableValues = "select * from employees"
        cur.execute(ReadingTableValues)
        data = cur.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])


        id = int(input("Enter Employee ID to Update : "))
        sal = float(input("Enter a salary to update :"))
        data = (sal,id)
        cur.execute(UpdatingTableValues,data)
        dbC.commit()
        print("Employee Details UPDATED Successfully...")
        print()

    elif o == 4:
        ReadingTableValues = "select * from employees"
        cur.execute(ReadingTableValues)
        data = cur.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])

        print("Enter the details to delete")    
        id = int(input("Enter ID to Delete Values : "))
        DeleteTableValues = "Delete from employees where id =%s"
        data = (id,)
        cur.execute(DeleteTableValues,data)
        dbC.commit()
        print("Employee Details DELETED Successfully...")
        print()

    elif o == 5:
        break

