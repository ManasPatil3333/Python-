str1 = 'Manas Kiran Patil'
upper = lambda string : string.upper()
print(upper(str1))

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))

cube = lambda y : y*y*y
print(cube(2))

even_odd = lambda num : f"is even" if(num%2 == 0) else f"is odd"
print(even_odd(cube(2))) 

list1 = [lambda args = x : args * 10 for x in range(1,5)]
for element in list1:
    print(element())

max = lambda num1, num2 : f"max : {num1}" if(num1>num2) else f"max : {num2}"
print(max(15,20))