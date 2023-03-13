# recursion is defining somethingh in terms of itself means we can define a function and that function will call that function again and again itself or in its own body


# example--- factorial of a number
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*fact(n-1))
print(fact(5))
