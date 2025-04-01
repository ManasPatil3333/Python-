
f = open('read.txt','r')
while(True) :
    text = f.readline()
    print(text)
    if not text :
        break
f.close()


# If you didn't close the file then it won't read the contents from the 'read.txt' file

# But their is a alternate method to work with the file without closing the file --->

# Use keyword 'with'

with open('read.txt','r') as f :
    while(True) :
        text = f.readline()
        print(text)
        if not text :
            break