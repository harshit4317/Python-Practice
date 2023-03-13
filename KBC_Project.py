#displying welcome message
print("Welcome To KBC")
questions=["ques_1","ques_2","ques_3"]
opt_ques_1=["a","b","c","d"]
length=len(questions)
for i in questions:
    match i:
        case 1:
            print(f"Your Question is:{i}")