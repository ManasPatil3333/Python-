dict1 = {"name":"Manas","age":18,"Gender":"male"}
dict2 = {"game":"Pokemon Go","mobile":"redmi note 11 pro"}
dict1.update(dict2)
print(dict1)
print(dict2)
print(dict1["name"])
'''
for key in dict1.keys() :
    print(key)
for value in dict1.values() :
    print(value)
'''
for key,value in zip(dict1.keys(),dict1.values()) :
    print(key,value)