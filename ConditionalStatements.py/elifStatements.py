n = int(input("Enter a number: "))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")


marks = int(input("Enter your marks :"))
if marks>=90:
    print("A Grade")
elif marks>=80 and marks<=89:
    print("B Grade")
elif marks>=70 and marks<=79:
    print("C Grade")
elif marks>=60 and marks<=69:
    print("D Grade")
elif marks>=50 and marks<=59:
    print("E Grade")
else:
    print("Fail")

marks = 10

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")