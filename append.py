f = open('append.txt','a')
print("Note : Type 'O' to add more notes or 'X' to end the notes.\n")
ch = input("Enter your command : ")
if(ch == 'O') :
    choice = bool(True)
else :
    choice = bool(False)
while(choice) :
    content = input("Enter content : ")
    f.writelines(content)
    ch = input("Type 'O' to add more notes or 'X' to end the notes : ")
    if(ch == 'O') :
        choice = bool(True)
    else :
        choice = bool(False)
        print("Done with the content.")