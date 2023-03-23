# set is used to store data items but in an unordered way and the elements in a set cannot be repeated it will return only once
a={1,2,3,4,1}
print(a)
b=set() #empty set
print(type(b))
for i in a:
    print(i)

b={"harshit","jarvis","tony"}


# union
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# isdisjoint is used to tell wheter a elements of a given set lies in another set if yes then it returns false
print(a.isdisjoint(b))

# superset-->tells that if the element of a set  lies in the orignal set then the orignal set is known as the supers set
# subset--> it tells the set is a subset of the superset when all the elements of a subset lies in a super set