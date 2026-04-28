# Task : 

# SINGLE INHERITANCE TASK

# Scenario: Online Course Platform
# Parent Class: Course
# course_name
# price

# method → show_course()

# Child Class: ProgrammingCourse
# language
# duration

# method → show_programming_course()

# Task:
# Create 2 programming courses
# Use super()
# Print all details
# Expected Thinking:
#  “Base course details reused + extra programming details added”



class Course:
    def __init__(self,course_name,price):
        self.course_name = course_name
        self.price = price

    def show_course(self):
        print("Course Name :",self.course_name)
        print("Price :",self.price)
    
        
class ProgrammingCourse(Course):
    def __init__(self, course_name,price,language,duration):
        super().__init__(course_name,price)
        self.language = language
        self.duration = duration

    def show_programming_course(self):
        super().show_course()
        print("Language :",self.language)
        print("Duration :",self.duration)

c1 = ProgrammingCourse("Data Science",35000,"Python","6 months")
c2 = ProgrammingCourse("Python Full Stack",30000,"Python","6 months")

c1.show_programming_course()
c2.show_programming_course()


   


# 🧬 2️⃣ MULTIPLE INHERITANCE TASK

# 🎯 Scenario: Smart Phone Features

# 👉 Parent 1: Camera
# camera_mp
# method → take_photo()

# 👉 Parent 2: MusicPlayer
# brand
# method → play_music()

# 👉 Child: SmartPhone
# model_name
# method → show_details()

# 🧑‍💻 Task:
# Create 2 smartphones
# Call both parent methods
# Print all features
# 👉 Goal:
#  Understand using multiple parents in one class


class Camera:
    def __init__(self,camera_mp):
        self.camera_mp=camera_mp

    def take_photo(self):
        print("Taking photo with ",self.camera_mp,"MP camera")
        
class MusicPlayer:
    def __init__(self,brand):
        self.brand=brand

    def play_music(self):
        print("Music Playing from",self.brand)

class SmartPhone(MusicPlayer,Camera):
    def __init__(self,camera_mp,brand,model_name):
        Camera.__init__(self,camera_mp)
        MusicPlayer.__init__(self,brand)
        self.model_name=model_name

    def show_details(self):
        print("Model :",self.model_name)
        print("Camera :",self.camera_mp)
        print("Music :",self.brand)

s1 = SmartPhone(50, "Sony", "Samsung Galaxy")
s2 = SmartPhone(108, "JBL", "OnePlus")

s1.show_details()
s1.take_photo()
s1.play_music()

print("------")

s2.show_details()
s2.take_photo()
s2.play_music()




# Task : 

# MULTILEVEL INHERITANCE TASK
# 🎯 Scenario: Education System
# 👉 Class 1: School
# school_name
# method → show_school()
# 👉 Class 2: Teacher (inherits School)
# teacher_name
# subject
# method → show_teacher()
# 👉 Class 3: Student (inherits Teacher)
# student_name
# grade
# method → show_student()


    
class School:
    school_name = "Sacred Heart High School"

    def show_school(self):
        print("School Name :",self.school_name)


class Teacher (School):
    teacher_name = "Ramesh"
    subject = "Maths"

    def show_teacher(self):
        print("Teacher Name :",self.teacher_name)
        print("Subject :",self.subject)

class Student (Teacher):
    student_name = "Thirumal"
    grade = 9.7
    def show_student(self):
        print("Student Name :",self.student_name)
        print("Grade :",self.grade)

obj = Student()
obj.show_student()
obj.show_teacher()
obj.show_school()


# ------------------------------------------(OR)------------------------------------------------------

    
class School:

    def show_school(self,school_name):
        self.school_name=school_name

        print("School Name :",self.school_name)


class Teacher(School):

    def show_teacher(self,teacher_name,subject):
        self.teacher_name=teacher_name
        self.subject=subject

        print("Teacher Name :",self.teacher_name)
        print("Subject :",self.subject)

class Student(Teacher):
    
    def show_student(self,student_name,grade):
        self.student_name=student_name
        self.grade=grade

        print("Student Name :",self.student_name)
        print("Grade :",self.grade)


obj = Student()
obj.show_school("Sacred Heart High School")
obj.show_teacher("Ramesh","Maths")
obj.show_student("Thirumal",9.7)


# 🧑‍💻 Task:
# Create 2 students
# Use super() in all classes
# Print full hierarchy details
# 👉 Goal:
#  Understand chain inheritance



class School:

    def show_school(self,school_name):
        self.school_name=school_name


class Teacher(School):

    def show_teacher(self,teacher_name,subject):
        self.teacher_name=teacher_name
        self.subject=subject


class Student1(Teacher):
    
    def show_student(self,student_name,grade):
        self.student_name=student_name
        self.grade=grade
        super().show_school(self.school_name)
        super().show_teacher(self.teacher_name,self.subject)

        print("School Name :",self.school_name)
        print("Teacher Name :",self.teacher_name)
        print("Subject :",self.subject)
        print("Student Name :",self.student_name)
        print("Grade :",self.grade)
        

class Student2(Teacher):
    
    def show_student(self,student_name,grade):
        self.student_name=student_name
        self.grade=grade
        super().show_school(self.school_name)
        super().show_teacher(self.teacher_name,self.subject)

        print("School Name :",self.school_name)
        print("Teacher Name :",self.teacher_name)
        print("Subject :",self.subject)
        print("Student Name :",self.student_name)
        print("Grade :",self.grade)


print("Student1")
obj = Student1()
obj.show_school("Sacred Heart High School")
obj.show_teacher("Ramesh","Maths")
obj.show_student("Thirumal",9.7)


print("\nStudent2")
obj = Student2()
obj.show_school("Sacred Heart High School")
obj.show_teacher("Mahender Reddy","Telugu")
obj.show_student("Naveen",9.0)



# ----------------------------------------------------------------------------------

class School:
    def __init__(self, school_name):
        self.school_name = school_name


class Teacher(School):
    def __init__(self, school_name, teacher_name, subject):
        super().__init__(school_name)
        self.teacher_name = teacher_name
        self.subject = subject


class Student1(Teacher):
    def __init__(self, school_name, teacher_name, subject, student_name, grade):
        super().__init__(school_name, teacher_name, subject)
        self.student_name = student_name
        self.grade = grade

    def display(self):
        print("School Name :", self.school_name)
        print("Teacher Name :", self.teacher_name)
        print("Subject :", self.subject)
        print("Student Name :", self.student_name)
        print("Grade :", self.grade)


class Student2(Teacher):
    def __init__(self, school_name, teacher_name, subject, student_name, grade):
        super().__init__(school_name, teacher_name, subject)
        self.student_name = student_name
        self.grade = grade

    def display(self):
        print("School Name :", self.school_name)
        print("Teacher Name :", self.teacher_name)
        print("Subject :", self.subject)
        print("Student Name :", self.student_name)
        print("Grade :", self.grade)


print("Student1")
s1 = Student1("Sacred Heart High School", "Ramesh", "Maths", "Thirumal", 9.7)
s1.display()

print("\nStudent2")
s2 = Student2("Sacred Heart High School", "Mahender Reddy", "Telugu", "Naveen", 9.0)
s2.display()



# HIERARCHICAL INHERITANCE TASK
# 🎯 Scenario: Food Delivery App
# 👉 Parent: User
# name
# location
# method → login()
# 👉 Child 1: Customer
# order_item
# method → place_order()
# 👉 Child 2: DeliveryPartner
# vehicle_type
# method → deliver_order()

class User:
    def __init__(self,Name,Location,Password):
        self.Name = Name
        self.Location = Location
        self.Password = Password

    def login(self,name,password):
        if self.Name == name and self.Password == password:
            print("Successfully Login!...")
            return True
        else:
            print("Invalid Password!...")
            return False

        
class Customer(User):

    def __init__(self,Name,Location,Password,order_item):
        super().__init__(Name,Location,Password)
        self.order_item=order_item

    def place_order(self):
        print(self.Name,"ordered",self.order_item)

    
class DeliveryPartner(User):
    def __init__(self,Name,Location,Password,vehicle_type):
        super().__init__(Name,Location,Password)
        self.vehicle_type = vehicle_type

    def deliver_order(self):
        print(self.Name,"is delivering through",self.vehicle_type)

    
customer = Customer("Thirumal","Hyderabad",12345678,"Biryani")
passwd = int(input("Enter Your Password :"))
if customer.login("Thirumal",passwd):
    customer.place_order()

print()

partner = DeliveryPartner("Naveen","Hyderabad",87654321,"Bike")
passwd = int(input("Enter Your Password :"))
if partner.login("Naveen",passwd):
    partner.deliver_order()



# 🧑‍💻 Task:
# Create 1 customer and 1 delivery partner
# Use super()
# Show login + role-specific actions
# 👉 Goal:
#  Same base class → different behaviors
