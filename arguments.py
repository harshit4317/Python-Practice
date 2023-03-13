# default arguments:- wjich have a parameters with predefined values and can be changed with giving new values as arguments while calling a function 
def avg(a=3, b=4):
    print("Average is",(a+b)/2)
avg() #default
avg(4,5) #arguments can also be changes by passing values while calling the function 

# required arguments:- when the values are not given to function parameters we have pass argumensts wile calling a function
def avg(a, b):
    print("Average is",(a+b)/2)
avg(4,5)

#infinite arguments:- when we want to pass many arguments 
# *--> will take arguemnts as tuple
# **--> will take arguemnts as list
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        
    print("Average is",sum/len(numbers))
average(4,5,6,7,8,9,344)

