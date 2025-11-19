my_tuple = (1,2,3,4)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-2])

my_tuple = (1,2,(10,20),4)
print(my_tuple[2][0])

my_tuple = list(my_tuple)
print(type(my_tuple))

t = (1,2,3)
x,y,z = t
print(x,y,z)

t = (1,2,3,1)
print(len(t))
print(t.count(1))
print(t.index(2))