def factorial(n) :
    '''Takes in a number and returns it's factorial.'''
    if(n==0 or n==1) :
        return 1
    else :
        return n*factorial(n-1)
    
num = int(input("Enter a number: "))
res = factorial(num)
print("factorial of",num,"is",res,"\n",factorial.__doc__)

def fibonacci(n) :
    '''Takes a number and returns it's fibonacci series.'''
    if(n==0 or n==1) :
        if(n==0) :
            return 0
        if(n==1) :
            return 1
    else :
        n1 = fibonacci(n-1)
        n2 = fibonacci(n-2)
        return (n1 + n2)
    
num1 = int(input("Enter a number: "))
res1 = fibonacci(num1)
print("fibonacci series of",num1,"is",res1,"\n",fibonacci.__doc__)