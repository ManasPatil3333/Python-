'''
f = open('write.txt','w')
text = input("Enter the content to store in 'write.txt' file :\n")
f.write(text)
f.close()
'''
# If you didn't close the file then it won't write the contents from the 'read.txt' file.

# But their is a alternate method to work with the file without closing the file --->

# Use keyword 'with' -->

with open('write.txt','w') as f :
    text = input("Enter the content to store in 'write.txt' file : \n")
    f.write(text)