try :
    num = int(input("Enter a number : "))
    print(f"Multiplication table of {num} :\n")
    for i in range(1,11) :
        print(f"{num} X {i} = {num*i}")
except :
    print("Something went wrong...")