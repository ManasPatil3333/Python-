a = True

print(a)
print(a := False)

numbers = [1,2,3,4,5]

while(n := len(numbers)) > 0 :
    print(numbers.pop())

foods = []
while (food := input("What would you like to eat?")) != "quit" :
    foods.append(food)