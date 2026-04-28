list = [1,2,3,4,5]
print(list)

l = ["orange","banana","apple"]
print(len(l))
print(l[1])
print(l[-1])

details = ["Thirumal",21,"Malla Reddy University"]
details.append(567)
details.remove(21)
details[1]=22
print(details)

c = ["cars","bikes","cycle"]
c.pop(1)
print(c)

a = [1,2,3,4]
b = [5,6,7,8]
a.extend(b)
print(a)

c = [7,6,5,4]
d = [1,2,3]
print(c[1:3])
print(c[::-1])
c.append(d)
print(c)

Fruits =  ["apple", "banana", "cherry"]
Fruits.append("pineapple")
print(Fruits)



l=[1,2,7,"apple",1.0,1.1,1.8,2.9,True,False]

l.append(5)
print(l)

l.extend(["banana",1.6,8])
print(l)

l.insert(2,"Vinay")
print(l)

l.reverse()  # asscending order
print(l)

l1 = [2,3,5,9,4]
l1.sort(reverse=True)   #desending order
print(l1)

l.remove(1.0)
print(l)

print(l.pop(1))
print(l)

l.pop()
print(l)


print(l.index("apple"))

print(l.count(1))


print(l.index(2))

l1 = [2,8,2,5,1]
l1.sort()
print(l1)


l = [29,3,1,8]
new_1 = l.copy()
print(new_1)


l.clear()
print(l)