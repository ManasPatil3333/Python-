# same as switch case ( use in Java , C , C++) but no need to use break statement in python.

import random # Random module is used.
list = ["Red", "Yellow", "Green"]
res = random.choice(list)
match res :
    case "Red" :
        print("Traffic signal : ",res, "\nYou need to stop...")
    case "Yellow" :
        print("Traffic signal : ",res, "\nGet ready to go...")
    case "Green" :
        print("Traffic signal : ",res, "\nYou are allow to go now...")
    case _:
        print("Don't move wait for the announcement...")


