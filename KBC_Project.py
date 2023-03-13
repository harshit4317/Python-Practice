questions={"ques1":"hello1","ques2":"hello2","ques3":"hello3","ques4":"hello4"}
options={"ques1":["a","b","c","d"],"ques2":["a","b","c","d"],"ques3":["a","b","c","d"],"ques4":["a","b","c","d"]}
answers={"ques1":"a","ques2":"c","ques3":"d","ques4":"a",}

def KBC():
    print("Welcome To KBC")
    for i in questions:
        print("Your Question is: ",questions[i])
        print(options[i])
        a=input("Enter your answer: \n")
        if a==(answers[i]):
            print("You won a Jackpot......")
        else:
            print("You lost the game")
            break
    print("Thank You for playing the game")


KBC()
