s = {1,2,3,7,9,7}
print(s)

s.add(8)
print(s)

s.remove(2)
print(s)

s.discard(3)
print(s)


nums = [1, 2, 2, 3, 4, 4]
unique = set(nums)
print(unique)


s = {1,5,3,7,4,8}

s.add(9)
print(s)

s.update([5,6])
print(s)

s.remove(1)
print(s)

s.discard(5)
print(s)

s.pop()
print(s)

s.clear()
print(s)


a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b))
print(b.union(a))

print(a.intersection(b))
print(b.intersection(a))

print(a.difference(b))
print(b.difference(a))

print(a.symmetric_difference(b)) 
print(b.symmetric_difference(a)) 


print(a.issubset(b))

print(a. issuperset(b))

print(a. isdisjoint(a))