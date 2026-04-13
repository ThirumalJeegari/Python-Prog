a = 20
b = 9.67
c = "10"
d = True
l = (1,2,3)
t = [4,8,9]
s= ([2,3,4])

print(float(a))
print(int(b))
print(int(c))
print(bool(d))
print(list(l))
print(tuple(t))
print(set(s))

print(list("1"))

print(str(55)+str(5))

print(bool(""))

print(int("100") + 50)

print(list("abc"))

print(set([1, 2, 2, 3]))

print(tuple([1, 2, 3]))

print(int(float("10.5")))     #print(int("10.5")) --> it will not directly convert string(float values in string) to int it can convert indirectly convert using float

print(int("10") + int("20") + int("30"))

print(bool("0"))

print(bool(""))

print(str(100) * 3)

print(set("hello"))

print("hello"*4)

print(int("101", 2))

print(int("110", 3))

a = 3.17
a = str(a)
print(a)
print(type(a))

a = "3.17"
a = int(float(a))
print(a)
print(type(a))