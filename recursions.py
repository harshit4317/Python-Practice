# recursion is defining somethingh in terms of itself means we can define a function and that function will call that function again and again itself or in its own body


# example--- factorial of a number
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return(n*fact(n-1))
# print(fact(5))
# n=int(input("Enter the number terms: "))



#fibonacci series
def fibonacci(n):
	if n<=1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

n = int(input('Enter a number: '))

fibo_series = []

for i in range(0,n):
	fibo_series.append(fibonacci(i))
	
print(fibo_series)

# f0=0 f1=1
# fn=fn-1+fn-2