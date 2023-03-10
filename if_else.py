age=int(input("Enter yor age "))
if(age<18):
    print("Your age is",age,"You are underage.")
else:
    if(age==18):
        print("Your age is",age,"Your age is perfect.")
    elif(age>18 and age<=30):
        print("Your age is",age,"Your age is perfect and between 18-30.")
    else:
        print("Your age is",age,"Your age is perfect and above 30.")

    