dict = {"name": "thirumal","age":21,"college":"MRU"}

print(dict["name"])

dict["age"] = 22

dict.pop("college")

print(dict)

print(dict.keys())

print(dict.values())


d = {
    "name":"Thirumal",
    "age":27,
    "College":"MRU",
    "Address":"Maisammaguda",
}

print(d.keys())

print(d.values())

print(d.items())


d.update({"name":"Vamshi","age":22})
print(d)

print(d.pop("Address"))
print(d)

print(d.popitem())

print(d.setdefault("College","Malla Reddy University"))
print(d)

new_d=d.copy()
print(new_d)

d.clear()
print(d)
