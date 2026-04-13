a = 100
b = 200
print(a<b and b>a)
print(a==10 and b!=200)


a=10
b=2
print(a==10 and b!=2)


c =1000
d = 200
print(c==10 or d==200)


a = True
print(not a)

a = 20
b =29
print(not(a==b))



# If a number is greater than 10 and less than 20, and the number is 15 — what is the result?

a = 15
print(a>10 and a<20)


# A number is 25. Check:
# Is it greater than 30 or less than 40?
# What will be the result?

a = 25
print(a>30 or a<40)



# A student passes if:
# marks ≥ 35 and attendance ≥ 75%
# If marks = 40 and attendance = 70%, will the student pass?

marks = 40
attendance = 70
student = marks >=35 and attendance >=75
if (student):
    print("pass")
else:
    print("fail")



# A person can vote if:
# age ≥ 18 and has ID proof
# If age = 20 but no ID proof, what is the result?

age =20
idProof = False
if age >=18 and idProof :
    print("Vote")
else:
    print("no vote")


