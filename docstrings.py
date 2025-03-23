# Docs strings should always be written on first line of function block.

def square(n) :
    '''takes in a number and return the square of the number.'''
    res = n*n
    print(res)
square(5)
print(square.__doc__)