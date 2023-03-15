# for loop with else is when the condition of for loop gets false or for loop ends due to the condition getting false then the else condition getv executed
# we can use it with while loop alsso
# suppose if we have a break statement in the for loop then the else statement will not get executed as here the loop is terminated or removed therefore the condition here is not getting false so the else statement will not get executed

for i in range(4):
    print(i)
else:
    print("hello")


    # with break
for i in range(4):
    print(i)
    if i==2 :
        break
else:
    print("sory")
    # here else statement will not be executed