# # Default Parameters:

# class Student:
#     def defaultconstructor(self):
#         pass
# a = Student()



# class Student:
#     def __init__(self):
#         print("Default Constructor!!")
# a = Student()


# class Student:
#     def __init__(self):
#         self.name = "Thirumal"
#         self.age = 21
# a = Student()
# print(a.name,a.age)



# class Student:
#     def __init__(self,name="Thirumal",age=21):
#         self.name = name
#         self.age = age
# a = Student()
# print(a.name,a.age)

# # ------------------------------------------------------------------------------

# # Parametrized Construction:

# class Student:
#     def __init__(self,a):
#         self.a=a
# obj = Student("Thirumal")
# print(obj.a)


# class Student:
#     def __init__(self,n,a=21):
#         self.name = n
#         self.age = a
# a = Student("Thirumal")
# print(a.name,a.age)

# -------------------------------------------------------------------------------------------------
# #Q1: Default Constructor

# # Create a class Laptop with a default constructor that sets:
# # brand = "HP"
# # price = 50000
# # 👉 Print the values.

# class Laptop:
#     def __init__(self):
#         self.brand = "Hp"
#         self.price = 50000
# o = Laptop()
# print(o.brand,o.price)


# #Q2: Parameterized Constructor

# # Create a class Student that takes:
# # name
# # marks
# # 👉 Print:
# # Name: Thirumal, Marks: 90

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
# o = Student("Thirumal",90)
# print("Name:"+o.name+", Marks:",o.marks)

# # Q3: Mixed Constructor (Tricky)

# # Create a class Employee:
# # name (required)
# # salary (default = 20000)
# # 👉 Test:
# # Employee("Ravi")
# # Employee("John", 50000)

# class Employee:
#     def __init__(self,name,salary=20000):
#         self.name = name
#         self.salary = salary
# o = Employee("Ravi")
# print(o.name,o.salary)

# t = Employee("John",50000)
# print(t.name,t.salary)


# #  Q4: Error Prediction
# # What will happen?

# class A:
#     def __init__(self, x):
#         self.x = x
# a = A()  #TypeError: __init__() missing 1 required positional argument: 'x'



# # Q5: Fix the Code
# class Car:
#     def __init__(self,name="BMW"):
#         self.name = name
# c = Car()
# print(c.name)

# # Q6: Constructor Calling Method
# # Create a class Welcome:
# # Constructor should print: "Welcome User"

# class Welcome:
#     def __init__(self):
#         print("Welcome User")
# a=Welcome()

# # Q7: Multiple Objects
# # 👉 Question: How many times constructor runs?

# class Test:
#     def __init__(self):
#         print("Constructor called")
# t1 = Test()
# t2 = Test()


# Default vs Parameterized
# 👉 Is this:
# Default constructor
# Parameterized constructor
# Both
# Explain.

# class Demo:
#     def __init__(self, x=10):
#         self.x = x
# a=Demo()
# print(a.x)


# ----------------------------------------------------------------------------------



# class MyClass:
#     name = "Thirumal"
#     age = 21
#     def student(self):
#         print(self.name)
#         print(self.age)   
# a=MyClass()
# a.student()
# print(a)



# class MyClass:
#     name = "Thirumal"
#     age = 21
#     def student(self):
#         print(self.name)
#         print(self.age)   
# print(MyClass())
# print(MyClass().student())



# class Student:
#     age = 21
#     name = "Vamshi"

#     def __init__(self,n,a,c,l):
#         self.name=n
#         self.age =a


#     def StudentDetails(self,n,a):
#         print(n,a)

#     def CollegeDetails(self):
#         cName = "Malla Reddy University"
#         cLoc = "Hyderabad"
#         print(cName,cLoc)

# o = Student("Vamshi",27,"Malla Reddy University","Hyd")
# o.StudentDetails("Thirumal",21)
# o.CollegeDetails()


# # Create a class Student with:
# # Class variable: school_name = "XYZ School"
# # A method set_details()
# #  → inside method, assign:
# # name = "Vamsi"
# # marks = 85
# # A method display()
# #  → print:
# # Name
# # Marks
# # School name
# # 👉 Outside the class:
# # Create object
# # Call set_details()
# # Call display()

# class Student():
#     school_name = "XYZ School"

#     def set_details(self):
#         self.Name = "Vamsi"
#         self.Marks = 85

#     def display(self):
#         print(self.Name)
#         print(self.Marks)
#         print(self.school_name)
# a=Student()
# a.set_details()
# a.display()






# # Create a class Employee with:
# # Class variable: company = "Infosys"
# # A method set_data()
# #  → assign:
# # name = "Ravi"
# # salary = 20000
# # A method increase_salary()
# #  → add 5000 to salary
# # A method display()
# #  → print all details
# # 👉 Outside the class:
# # Create object
# # Call all methods


# class Employee:
#     company = "Infosys"

#     def set_data(self):
#         self.name = "Ravi"
#         self.salary = 20000

#     def increase_salary(self):
#         self.salary+=5000

#     def display(self):
#         print(self.name)
#         print(self.salary)
#         print(self.company)

# a = Employee()
# a.set_data()
# a.increase_salary()
# a.display()



# # Create a class Mobile with:
# # Class variable: brand = "Apple"
# # A method set_details()
# #  → assign:
# # model = "iPhone 14"
# # price = 80000
# # A method discount()
# #  → reduce price by 10%
# # A method show_details()
# #  → print all details
# # 👉 Outside the class:
# # Create object
# # Call methods


# class Mobile:
#     brand = "Apple"

#     def set_details(self):
#         self.model = "iPhone 14"
#         self.price = 80000

#     def discount(self):
#         self.price *= 0.9

#     def show_details(self):
#         print(self.brand)
#         print(self.model)
#         print(int(self.price))

# a = Mobile()
# a.set_details()
# a.discount()
# a.show_details()





# class Myclass:
#     a = 10
#     c = "Car"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def Mymethod(self,college,location):
#         self.college = college
#         self.location = location
# obj = Myclass("Thirumal",21)
# obj.Mymethod("MRU","HYD")
# print(obj.name,obj.age)
# print(obj.college,obj.location)



# # Real-World Class & Object Test
# # 🏦 Q1: Bank Account (Basic)
# # 🔹 Requirements

# # Create a class BankAccount:

# # Constructor:
# # account_holder
# # balance
# # 🔹 Methods
# # deposit(amount) → add money
# # withdraw(amount) → subtract money
# # display() → print details

# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         print("Deposite :",amount)

#     def withdraw(self,amount):
#         if self.balance <=0:
#             print("Insufficent Balance")
#         else:
#             self.balance -=amount
#             print("Withdraw :",amount)
#     def display(self,):
#         print("Account_Holder :",self.account_holder)
#         print("Balance :",self.balance)
        
# acc = BankAccount("Thirumal",50000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.display()




# Q2: Student System
# Requirements
# Create class Student:
# Constructor:
# name
# marks (single value)
# Methods
# display() → print name & marks
# result() →
# ≥ 50 → Pass
# < 50 → Fail

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("Name :",self.name)
#         print("Marks :",self.marks)
#     def result(self):
#         if self.marks < 0 or self.marks > 100:
#             print("Invalid Marks")
#         elif self.marks >=50:
#             print("Pass")
#         else:
#             print("Fail")

# o = Student("Thirumal",86)
# o.display()
# o.result()




# # Car Details
# # 🔹 Requirements
# # Create class Car:
# # Constructor:
# # brand
# # price
# # 🔹 Method
# # show() → print details

    
# class car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

#     def show(self):
#         print(self.brand)
#         print(self.price)
# a = car("Bentely",20000000)
# a.show()


# # Mobile
# # 🔹 Requirements
# # Create class Mobile:
# # Constructor:
# # brand
# # price
# # 🔹 Methods
# # discount() → reduce price by 10%
# # display() → show updated price

# class Mobile:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#     def discount(self):
#         self.price = self.price-(self.price*0.10)    #self.price *= 0.90
#     def display(self):
#         print("Brand :",self.brand)
#         print("Price :",self.price)
# o = Mobile("Realme",17000)
# o.discount()
# o.display()



# Q5: Employee
# 🔹 Requirements
# Create class Employee:
# Constructor:
# name
# salary
# 🔹 Methods
# increase_salary() → add 2000
# display()

class Employee:
    def __init__(self,name,salary):
        self.name =name
        self.salary=salary
    def increase_salary(self):
        self.salary = self.salary + 2000
    def display(self):
        print(self.name)
        print(self.salary)


a = Employee("Thirumal",30000)
a.increase_salary()
a.display()

