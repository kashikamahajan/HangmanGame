import random
list=['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grapefruit', 'honeydew']
word=list[random.randint(0,len(list)-1)]

str=""

vowels=['a','e','i','o','u']
for i in range(0,len(word)):
    if word[i] in vowels:
        str=str+word[i]
    else:
        str=str+"_"


print(str)

guess=[]
hg="HANGMAN"
trys=0
letter=""
flag=False

letters=[]
for i in range(0,len(str)):
    letters.append(str[i])


while hg[len(hg)-1]=="N" or str==word:
    print( )
    print("__________________________________________")
    flag=False
    print(hg)
    print(str)
    print(guess)
    letter=input("Enter a letter: ")

    if letter in guess:
        print("Already tried that!")
        continue
    guess.append(letter)

    for i in range(0,len(word)):
        if word[i]==letter:
            letters[i]=letter
            flag=True
            
    
    if flag==False:
        hg=hg.replace(hg[trys],"*",1)
        trys=trys+1

    str=''.join(letters)
    
    if str==word:
            break
    

print("Game ended")


        


