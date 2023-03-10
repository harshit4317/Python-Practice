import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))
if(hour>=5 and hour<12):
    print("Good Morning :)")
elif(hour>=12 and hour<16):
    print("Good Afternoon `.`")
elif(hour>=16 and hour<20):
    print("Good Evening :)")
else:
    print("Good Evening -.-")


