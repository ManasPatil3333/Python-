# For loops :
'''
name = "Manas"
for ch in name :
    print(ch)
'''
# Nested for loops :
'''
list = ("RED", "YELLOW", "GREEN")
for color in list :
    print(color)
    for letter in color :
        print(letter)
'''
# For loops using range :
'''
for m in range(5) :
    print(m)
for m in range(2,6) :
    print(m)
for m in range(0,31,3) :
    print(m)

list1 = ("Apple", "Banana", "Guava")
list2 = ("red", "yellow", "green")
for fruit, color in zip(list1,list2) :
    print(fruit, " is ", color)
'''
# while loops :

num = int(input("Enter a number : "))
m = num
while(m<10) :
    print(m)
    m = m + 1
else :
    print(num)

# For loop with else statement :

for i in range(5) :
    print(i) 
else :
    print("sorry, no value of i")

name = "manas"

for index,letter in enumerate(name) :
    print(index+1,". ",letter)