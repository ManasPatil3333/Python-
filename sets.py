# Do not allow duplicate values or elements,

# set type of container is unordered, the output changes everytime

set = {4,2,6,2,10,8}
print(set)

# 1. add() : add elements at the end of the set
set.add(11)
print(set)

# 2. remove() : remove element from the set
set.remove(4)
print(set)

# 3. pop() : remove a element from the start of the set
set.pop()
print(set)

# 4. discard() : delete a element from the start
set.discard(8)
print(set)

# 5. clear() : delete or clear all elements of set
set.clear()
print(set)

# 6. union() :
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
print(set1.union(set2))

# 7. intersection() :
print(set1.intersection(set2))
print(set1)
print(set2)

print(set1.isdisjoint(set2))

# disjoint : values in both sets should be different

# superset : all values of one set should be present in other set
