a= int(input("Enter number:\n"))
b= int(input("Enter number:\n"))
c=input("Choose one opertaor from the following operator:\n\"+, -, *, /, //, %, power\"\nEnter the operator: ")
if(c=='+'):
    print(a,c,b,"=",a+b)
elif(c=='-'):
    print(a,c,b,"=",a-b)
elif(c=='*'):
    print(a,c,b,"=",a*b)
elif(c=='/'):
    print(a,c,b,"=",a/b)
elif(c=='//'):
    print(a,c,b,"=",a//b)
elif(c=='%'):
    print(a,c,b,"=",a%b)
elif(c=='power'):
    print(a,c,b,"=",a**b)
else:
    print("Invalid operator used.\nPlease use the right operator.")
