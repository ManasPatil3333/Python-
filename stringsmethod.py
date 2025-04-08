str1 = "manas"
print(len(str1))
print(str1[0:])
print(str1[0:3])
print(str1[0:-3])

# strings are immutable!!!

str = "my name is >>>>> Manas Kiran Patil >>>>>>>>>>>>"
print(str.upper())
print(str.lower())
print(str.replace("my name is ","I am "))
print(str.rstrip(">"))
print(str.split(" "))
str2 = "introduction to python"
print(str2.capitalize())
print(len(str2))
print(str2.center(50))
print(str.count("a"))
print(str.endswith(">"))
print(str.endswith("name",3,7))
print(str.endswith("name",4,7))
print(str.endswith("name",0,10))
print(str.find(">"))
print("\n")

str3 = "BMWM5"
str4 = "BMW M5"
str5 = "<<BMWM5>>"
# alphanumerical means a string that contains a-z , A-Z , 0-9 .
print(str3.isalnum())
print(str4.isalnum())
print(str5.isalnum())
print("\n")

str6 = "MANAS"
str7 = "manas"
print(str6.islower())
print(str7.islower())
print(str6.isupper())
print("\n")

str8 = "I am Manas Kiran Patil"
str9 = "I am Manas Kiran Patil\n"
str10 = "I am Manas Kiran Patil>"
str11 = "IamManasKiranPatil"
str12 = "   "
print(str8.isprintable())
print(str9.isprintable())
print(str10.isprintable())
print(str12.isspace())
print(str11.isspace())
print("\n")

str13 = "World Health Organization"
str14 = "Manas kiran Patil"
print(str13.istitle())
print(str14.istitle())

print(str8.swapcase())

str15 = "i am manas kiran patil"
print(str15.title())