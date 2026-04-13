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