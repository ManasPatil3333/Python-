print("Simple Calculator....")
num1 = input("Enter the first number : \n")
num2 = input("Enter the second number : \n")
print("Enter '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division and '%' for mod.")
decision = input()
if decision == '+':
    print("solution : ", int(num1)+int(num2))
elif decision == '-':
    print("solution : ", int(num1)-int(num2))
elif decision == '*':
    print("solution : ", int(num1)*int(num2))
elif decision == '/':
    if num2 == 0 :
        print("Error, denominator can't be zero.")
    else :
        print("solution : ", int(num1)/int(num2))
else :
    if num2 == 0 :
        print("Error, denominator can't be zero.")
    else :
        print("solution : ", int(num1)%int(num2))

