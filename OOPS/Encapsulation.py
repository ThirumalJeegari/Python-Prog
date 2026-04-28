# # Create a class Product
# # Create private variable for price
# # Add method set_price(price)
# # Accept only values greater than 0
# # Add method apply_discount(percent)
# # Discount should not exceed 50%
# # Update price after discount
# # Add method get_price()
# # Return current price


# class Product:
#     def __init__(self,price):
#         self.__price =0
#         self.set_price(price)

#     def set_price(self,price):
#         if price > 0:
#             self.__price=price
#         else:
#             print("price <= 0")

#     def apply_discount(self,percent):
#         if 0 < percent <=50:
#             discount = (self.__price * percent) / 100
#             self.__price -= discount
#         else:
#             print("Discount should be between 0 to 50")

#     def get_price(self):
#         return self.__price
    

# o = Product(400)
# o.set_price(500)
# o.apply_discount(10)
# print(o.get_price())




# # Encapsulation Task 2: Mobile Lock System
# #  Instructions:
# # Create a class Mobile
# # Create private variable for password
# # Add method set_password(pwd)
# # Password must be at least 4 characters
# # Add method unlock(pwd)
# # Check password and print result
# # Add method change_password(old_pwd, new_pwd)
# # Change only if old password is correct
# # New password must follow rules




# class Mobile:
#     def __init__(self,password):
#         self.__password = None
#         self.set_password(password)

#     def set_password(self,pwd):
#         if len(str(pwd)) >= 4:
#             self.__password = pwd
#         else:
#             print("Password must be at least 4 characters")

#     def unlock(self,pwd):
#         if self.__password == pwd:
#             print("Unlocked")
#         else:
#             print("Wrong Password Entered!")
    
#     def change_password(self,old_pwd,new_pwd):
#         if self.__password == old_pwd:
#             if len(str(new_pwd)) >=4:
#                 self.__password = new_pwd
#                 print("Password changed")
#             else:
#                 print("Password Not changed")
#         else:
#             print("wrong password")

# o = Mobile(int(input("Set Password :")))    
# o.unlock(int(input("Enter Password :")))
# o.change_password(int(input("Enter old Password :")),int(input("Enter new Password :")))
# o.unlock(int(input("Enter Password :")))





# Encapsulation Task 3: HR Employee System
# Instructions:
# Create a class Employee
# Create private variables:
# __salary
# __designation
# Add method set_salary(salary)
# Salary should be greater than 0
# Prevent invalid updates
# Add method get_salary()
# Return salary
# Add method set_designation(role)
# Allow only specific roles (e.g., "Manager", "Developer", "HR")
# Add method get_designation()
# Return designation
# Add method increment_salary(percent)
# Increase salary based on percentage
# Percentage should not exceed 30%
# Do not allow direct access to salary or designation from outside the class



class Employee:
    def __init__(self):
        self.__salary = 0
        self.__designation =None

    def set_salary(self,salary):
        if salary > 0:
            self.__salary =salary
        else:
            print("Invalid Salary")

    def get_salary(self):
        return self.__salary
    
    def set_designation(self,role):
        if role == "Manager" or role == "Developer" or role == "HR":
                self.__designation = role
        else:
            print("Invalid designation")

    def get_designation(self):
        return self.__designation 
      
    def increment_salary(self,percent):
        if 0 < percent <= 30:
            increment = (self.__salary * percent) /100
            self.__salary +=increment
        else:
            print("Increment should be between 0 and 30%")

o = Employee()
o.set_salary(50000)
print("Enter the salary :",o.get_salary())
o.set_designation("Developer")
print("Enter the Designation :",o.get_designation())
o.increment_salary(int(input("Enter the percentage to increment the salary upto 30% :")))
print("Your Updated salary :",o.get_salary())


