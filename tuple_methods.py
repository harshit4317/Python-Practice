#tuple is immutable means it can  not be changed but we can change the values of tuple by converting the tuple into losit first than converting it back to tuple 
tup_a=(20,30,50,6,8,6,5)
print(tup_a)
list_a=list(tup_a)#converting the tuple in list
list_a.append(200)
print(list_a)
tup_a=tuple(list_a)#converting it in tuple back
print(tup_a)


# to access the elements of tuple at following index
tup_2=(1,2,3,3,5,6,7,4,2,1,42,5,)
print(tup_2.index(1,3))