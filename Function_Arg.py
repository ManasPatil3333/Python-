def average (a,b) :
    avg = (a+b)/2
    print("Average : ", avg)

def average(*numbers) : # Here * indicates that container is a tuple
    sum = 0
    for num in numbers :
        sum = sum + num
    avg = sum/len(numbers)
    return avg

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))
num4 = int(input("Enter a number : "))
res = average(num1,num2,num3,num4)
print("Average : ", res)

# For creating a dictionary container then type '**' 2 asterik signs!  
# For creating a tuple containers then type '*' one asterik sign!