# Lists is muttable
"""
list1 = ("manas", "kiran", "patil", 1, 2, 3)
print(list1)
for i in list1 :
    print(i)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print(list1[1:4])
print(list1[0:5:2])
"""

# Lists methods :

list = ["Apple", "Banana", "Pineapple", "Mango"]
print(list)

# 1. append(element) :
list.append("Guava")
print(list)

# 2. insert(pos, element) :
list.insert(0,"Watermelon")
print(list)
list1 = ["Carrot", "Raddish", "onion"]

# 3. list1_name.extend(list2_name) : 
list.extend(list1)
print(list)

# 4. sum(list_name) : Add all the elements in a list.
list2 = [12, 12, 24]
print(sum(list2))

# 5. count(element) : Gives the total occurence of a particular element in a list.
print(list2.count(12))

# 6. len(list_name) : Gives the length of the list.
print(len(list2))

# 7. index(element) : gives the first occurence of the element.
list3 = ["manas", "kiran", "patil", "kiran"]
print(list3.index("kiran"))

# 8. min(list_name) : gives the minimum element in a list.
list4 = [1,4,6,2,3]
print(min(list4))

# 9. max(list_name) : gives the maximum element in a list.
print(max(list4))

# 10. list_name.sort() : sort the list in ascending order.
list4.sort()
print(list4)

# 11. list_name.reverse() : sort the list in descending order.
list4.reverse()
print(list4)

# 12. pop() : Remove an element from a list. ( with respect to list's element's position. )
list4.pop(2)
print(list4)
list4.pop()
print(list4)

# 13. remove() : remove an element from a list. ( with respect to list's element's identity. )
list4.remove(6)
print(list4, "Done")
