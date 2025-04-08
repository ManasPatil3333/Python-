# conditional operators : ( > , < , <= , >= , == , != )

num = int(input("Enter the number : "))
if (num > 0) :
    print("Entered number is positive.")
elif (num == 0) :
    print("Entered number is zero.")
else :
    print("Entered number is negative.")

a = int(input("Enter a number : "))
b = int(input("Enter a anoother number : "))

print(f"{a} is greater than {b}") if (a>b) else  print(f"{a} is equal to {b}") if (a==b) else print(f"{b} is greater than {a}")