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






    



