# dictionary is used to store data items but in ordered manner each data items has a key with its value pair


dict={"name":"harshit","age":24}
# accesing items
print(dict.items())

# accesing keys
print(dict.keys())
# accesing values
print(dict.values())

a={"name":"harshit","age":24}
b={1:2,3:4}
a.update(b) #-->will store a and b contents combined in a
print(a)

print(a.popitem())
print(a)