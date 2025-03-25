def calculateGmean(a,b) :
    mean = (a*b)/(a+b)
    print("Geometric mean of given values is ", mean)

def isGreater(a,b) :
    if (a>b) :
        print(a, " is greater number than ",b)
    else :
        print(b, " is greater number than ",a)

def isLesser(a,b) :
    pass 

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
calculateGmean(num1, num2)
isGreater(num1, num2)

num3 = int(input("Enter the first number : "))
num4 = int(input("Enter the second number : "))
calculateGmean(num3, num4)
isGreater(num3, num4)

