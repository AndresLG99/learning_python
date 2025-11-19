my_set = set([1,2,3,4,5])
print(type(my_set))
print(my_set)

other_set = {1,2,3,4,5}
print(type(other_set))
print(other_set)

other_set = {1,2,3,4,5,1,1,1,(1,2,3),2,2,2,2,3,3,4,4,5,5,5,5}
print(type(other_set))
print(other_set)

print(len(other_set))
print(2 in other_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s4 = s1 | s2
print(s4)

s5 = s1 & s2
print(s5)

s6 = s1 ^ s2
print(s6)

s1.add(6)
print(s1)

s1.remove(6)
print(s1)

s1.discard(6)
print(s1)

s1.pop()            # Random
print(s1)

s1.clear()
print(s1)