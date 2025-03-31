x = 100 # Here 'x' is a global variable

def function() :
    # global x # ( first run without '#' comment sign )
    x = 5 # here 'x' is a local variable because is defined in a block of function 
    y = 10 # 'y' is also a local variable and only be operated within this block of function

    # Local variable are terminate or destroy as the code(block) of the function ends

    print(y)

function()
print(x) # the output is 100
# print(y) : printing the value of y here will create error because local variable can't be operate outside the block of the function

# but we can change the value of global variable in a block of code by using keyword 'global' in block of function 
 
