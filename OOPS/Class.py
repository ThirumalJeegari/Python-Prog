class MyClass:
    name = "Thirumal"
    age = 21
    def student(self):
        print(self.name)
        print(self.age)   
a=MyClass()
a.student()
print(a)

class MyClass:
    name = "Thirumal"
    age = 21
    def student(self):
        print(self.name)
        print(self.age)   
print(MyClass())
print(MyClass().student())



class Student:
    age = 21
    name = "Vamshi"

    def __init__(self,n,a,c,l):
        self.name=n
        self.age =a


    def StudentDetails(self,n,a):
        print(n,a)

    def CollegeDetails(self):
        cName = "Malla Reddy University"
        cLoc = "Hyderabad"
        print(cName,cLoc)

o = Student("Vamshi",27,"Malla Reddy University","Hyd")
o.StudentDetails("Thirumal",21)
o.CollegeDetails()


# Create a class Student with:
# Class variable: school_name = "XYZ School"
# A method set_details()
#  → inside method, assign:
# name = "Vamsi"
# marks = 85
# A method display()
#  → print:
# Name
# Marks
# School name
# 👉 Outside the class:
# Create object
# Call set_details()
# Call display()

class Student():
    school_name = "XYZ School"

    def set_details(self):
        self.Name = "Vamsi"
        self.Marks = 85

    def display(self):
        print(self.Name)
        print(self.Marks)
        print(self.school_name)
a=Student()
a.set_details()
a.display()






# Create a class Employee with:
# Class variable: company = "Infosys"
# A method set_data()
#  → assign:
# name = "Ravi"
# salary = 20000
# A method increase_salary()
#  → add 5000 to salary
# A method display()
#  → print all details
# 👉 Outside the class:
# Create object
# Call all methods


class Employee:
    company = "Infosys"

    def set_data(self):
        self.name = "Ravi"
        self.salary = 20000

    def increase_salary(self):
        self.salary+=5000

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.company)

a = Employee()
a.set_data()
a.increase_salary()
a.display()



# Create a class Mobile with:
# Class variable: brand = "Apple"
# A method set_details()
#  → assign:
# model = "iPhone 14"
# price = 80000
# A method discount()
#  → reduce price by 10%
# A method show_details()
#  → print all details
# 👉 Outside the class:
# Create object
# Call methods


class Mobile:
    brand = "Apple"

    def set_details(self):
        self.model = "iPhone 14"
        self.price = 80000

    def discount(self):
        self.price *= 0.9

    def show_details(self):
        print(self.brand)
        print(self.model)
        print(int(self.price))

a = Mobile()
a.set_details()
a.discount()
a.show_details()





