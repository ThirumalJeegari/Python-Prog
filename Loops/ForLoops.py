for i in "Thirumal":
    print(i)

for i in [1,2,3,4,5]:
    print(i)

for i in (1,3,5,6):
    print(i)

for i in {"id": 567 ,"name":"Thirumal"}:
    print(i)

for i in {"id": 567 ,"name":"Thirumal"}.values():
    print(i)

for i in {"id": 567 ,"name":"Thirumal"}.items():
    print(i)

for i,j in {"id": 567 ,"name":"Thirumal"}.items():
    print(i,j)


#--------------------  using range() -----------------------



for i in range(1,11,1):         #(start,end,step)
    print(i)

for i in range(10,0,-1):
    print(i)




sumofevennumbers = 0
sumofoddnumbers = 0
for i in range(1,11,1):
    if i%2==0:
        sumofevennumbers +=i
    else:
        sumofoddnumbers +=i
print(sumofevennumbers,"is a Even number")
print(sumofoddnumbers,"is a Odd number")


vowels ="aeiouAEIOU"
name = "Thirumal"
count = 0
for i in name:
    if i in vowels:
        count +=1
        print(i,end=" ")
print()
print(count,"count of vowels")




for i in range(-1,-101,-1):
    print(i)

for i in range(-100,0,1):
    print(i)