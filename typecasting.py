# typecasting is used to convert one data type into another data typ. type casting is of two type :-
# 1.) implicit: python convert the small data type in larger data type to avoid data loss
# 2.) explicit: in this developer ask the python to convert it into another data type

# implicit
a=2
c=4.666
print(a+c)
# in this out is float but a is only int so it is converted into larger datatype float 


# explicit
a=int("1")
b="2"
print(a+int(b))

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  # return 7
#   return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
# print(c)