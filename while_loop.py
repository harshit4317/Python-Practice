a=5
while(a> -1):
    print(a)
    a=a-1

else:
    print("loop is finished")



# break and continue
a=2
i=1
while(i<=12):
    print(a,"*",i,"=",(a*i))
    i+=1
    if(i>10):
        break