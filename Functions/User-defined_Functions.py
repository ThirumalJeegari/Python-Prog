# # User-defined functions are functions that are created by the programmer to perform a specific task, instead of using pre-built (built-in) functions.



# def add(a, b): # parameters
#     return a + b
# c = add(5, 3)  # arguments
# print(c)

# #-----(OR)-----------------------------------

# def add(a, b): # parameters
#     return a + b
# print(add(5, 3))  # arguments





# def add():
#     a = 10
#     b = 20
#     print(a+b)
# add()






# def mul():
#     a = 10
#     b = 20
#     print(a*b)
# mul()





# # Registration
# def register():
#     n = input("Enter a name :")
#     e = input("Enter a email :")
#     p = input("Enter a password :")
#     cp = input("Conform a password :")

#     if p == cp :
#         print("Registration Successfully....")
#     else:
#         print("Registration Not Successfull")
# register()





# def dashboard():
#     print("Welcome to Dashboard")  
# dashboard()

# # Login
# def login():
#     er="vamsi@gmail.com"
#     pr="12345678"
#     e=input("enter email here :--  ")
#     p=input("enter password :-- ")

#     if e == er and p == pr :
#         print("login successful")
#         dashboard()
#     else:
#         print("invalid credentails")
# login()  





# # default parameters 

# def greet(name="Guest"):
#     print("Hello", name)
# greet()
# greet("Thirumal")





# def greet(name=""):
#     print("Hello",name)
# greet()
# greet("Thirumal")





# def value(a=1,b=2,c=3):
#     return a+b+c
# print(value())




# def value(a=1,b=2,c=3):
#     print(a+b+c)
#     return a+b+c
# print(value())




# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# demo(1, 2, 3, name="Thirumal", age=21)




# def demo(*args, **kwargs):
#     return args,kwargs
# print(demo(1, 2, 3, name="Thirumal", age=21))



# def abc(*xyz):
#     print(xyz)
# abc(1,2,3,4,5)




# x = 10  # global
# def show():
#     y = 5  # local
#     print(x, y)
# show()





# def abcd(a,b,c,d):
#     print(a,b,c,d)
# abcd("vamsi",20,[1,2,3,4,5,6],{"id":1})  

# # Recursion
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))


# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner

# func = outer()
# func()

import sys
print(sys.getrecursionlimit())  #recursion limit in Python