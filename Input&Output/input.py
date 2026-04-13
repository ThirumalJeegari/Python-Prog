name = input("Enter a name : ")
print("You Entered a name :",name,end="")
print()


a = input("Enter a number : ")          # input() defaults it takes string 
print("You Entered :",a)
print(type(a))


a = input("Enter a number : ")          # input(string values) is converted to integer
b = int(a)
print("You Entered :",a)
print(type(b))


a = int(input("Enter a number : "))     
print("You Entered :",a)
print(type(a))

a = float(input("Enter a number : "))     
print("You Entered :",a)
print(type(a))

name = input("Enter a name :")
age = int(input("Enter a age :"))
print("Your name is "+name+" and Your age is",age)  # +name+ is a concatenation and it works only on string

