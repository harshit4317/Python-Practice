# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end then reverse the string
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end.

# Your program should ask whether you want to code or decode





# code
import random
def secret_code():
    opt=input("what you want Encode or Decode. Choose \nE:Encode \nD:Decode\n")
    if(opt=="E"):
        string=input("Enter here. Please!\n")
        # splitting words of the input given
        words=string.split()
        print(words)
        # making a list that will be used to add words to make our secret code
        randomlist=["abc","xyz","cfd","hyf","hfg","hga","klh","rtw","fhj","fhj","hjj","fdh","ljg","lkj","fgm","dnk","twe","lsj","fwq","fhn","erg","cvb","bsh","whw","hds","jrt","wrh","htr","whs","wht"]
        new_x=[]
        for i in words:
            if(len(i)>=3):
                starting_word=i[0]
                # removing the first letter of thw word from string
                x=i.replace(i[0],"")
                # adding the first letter at the end of the new word
                x=x+starting_word
                # adding the 3 words at the beginning and ending of the word
                x=random.choice(randomlist)+x+random.choice(randomlist)
                # print(x)
                # reversing the word
                reversed_string=x[::-1]
                print(reversed_string)
                new_x.append(reversed_string)
            # reversing the string if length is less than 3
            else:
                reverse_string=i[::-1]
                new_x.append(reverse_string)
        print(new_x)
        new_string=" ".join(new_x)
        print(new_string)
    
    
    elif(opt=="D"):
        string=input("Enter the encoded string here. Please!\n")
        words=string.split()
        print(words)
        new_x=[]
        for i in words:
            if(len(i)>=3):
                x=i[3:-3]
                starting_word=x[0]
                x=x.replace(x[0],"")
                #reversing the word
                x=x[::-1]
                x=starting_word+x
                new_x.append(x)
        #     # reversing the string if length is less than 3
            else:
                reverse_string=i[::-1]
                new_x.append(reverse_string)
        #giving the decoded string
        new_string=" ".join(new_x)
        print(new_string)

secret_code()