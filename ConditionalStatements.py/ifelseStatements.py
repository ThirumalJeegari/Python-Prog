age = int(input("Enter your age :"))
if age>=18:
    print("your are eligible to vote!.")
else:
    print("Your are not eligible to vote")

if (True):
    print("True")           # "True"
else:
    print("False")

if (True):
    print(True)               # True
else:
    print(False)



num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Even number")

else:
    print("Odd number")



age = int(input("Enter your age :"))
if age>=18:
    print("your are eligible to drive")
else:
    print("Your are not eligible to drive")



marks = int(input("Enter your marks :"))
if marks>=50:
    print("Pass")
else:
    print("Fail")

n = int(input("Enter a number :"))
if(n%3==0 and n%5==0):
    print(n,"Divisible by 3 and 5")
else:
    print(n,"is not divisible by both 3 and 5")

a =int(input("Enter a value :"))
b =int(input("Enter  b value :"))
if (a>b):
    print(a,"is maximum value")
else:
    print(b,"is maximum value")

year = int(input("Enter a number :"))
if( year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):     #if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year,"is a  leap year")
else:
    print(year,"not a leap year")



a = int(input("Enter a sides :"))
b = int(input("Enter b sides :"))
c = int(input("Enter c sides :"))
if a+b>c and b+c>a and c+a>b:
    print("It is a Triangle")
else:
    print("It is not a triangle")



a = int(input("Enter a sides :"))
b = int(input("Enter b sides :"))
c = int(input("Enter c sides :"))
print("Valid" if a+b>c and a+c>b and b+c>a else "Invalid")


a = int(input("Enter a sides :"))
b = int(input("Enter b sides :"))
c = int(input("Enter c sides :"))
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


num = int(input("Enter a number : "))
if (num>=10 and num<=50):
    print("inclusive")
else:
    print("exclusive")




if 10 <= num <= 50:
    print("inclusive")
else:
    print("exclusive")

digit =(input("Enter a number : "))             #it consider as a string data type
if len(digit)==3:
    print("It is a three digit number")
else:
    print("It is not a three digit number")


digit =int(input("Enter a number : "))          
if (100<=abs(digit)<=999):                          # abs() = absloute value which means converts negative values to positive values
    print("It is a three digit number")
else:
    print("It is not a three digit number")

