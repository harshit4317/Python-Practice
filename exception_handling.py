# try except statement is used to find and throw and error from a code of bloc try is used were the error can be thrown and except statement is used to show the error the error can be of various types and can be defined by user too.
def check():
    try:
        a=int(input("Enter the number \n"))
        b=[10,20,30,40]
        print(b[a])
    except ValueError:
        print("Invaild input")
        # finally keyword is used to run the commands even the code in the try catch throws error, it is mainly used in the function when we have a return statement as in  a funtion the function stops after excetuing the return statement so the simple print ststaemnet will not get executed 
    finally: 
        print("Always Exceuted")
a=check()

# use of finally using the return in statement
def check():
    try:
        a=int(input("Enter the number \n"))
        b=[10,20,30,40]
        print(b[a])
        return 1
    except ValueError:
        print("Invaild input")
        return 0 #will return 0 when the code throws error
    finally: 
        print("Always Exceuted")
    print("Not Always Exceuted") #this statement will not get executed as the function will end giving the return a=statement but the finally statement will executed
a=check()



# raising an error--> we can rasie an custom aerror useing raise command it is used to throw error immediately after the code
a= input("Enter the number\n")
if(a=="quit"):
    print("ok")
elif(int(a)<5 or int(a)>9):
    raise ValueError("Your no. is between 5 and 9")
print("thankyou")
