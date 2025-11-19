my_list = ["a","b","c"]
my_list2 = ["d","e","f"]
my_list3 = my_list + my_list2

print(type(my_list))

result = len(my_list)
print(result)

result = my_list[0]
print(result)

result = my_list[0:2]
print(result)

print(my_list + my_list2)
print(my_list3)

my_list3[0] = "alpha"
print(my_list3)

my_list3.append("g")
print(my_list3)

my_list3.pop()
print(my_list3)

my_list3.pop(0)
print(my_list3)

deleted = my_list3.pop(0)
print(my_list3)
print(deleted)

new_list = ["g","o","b","m","c"]
new_list.sort()                     # Can't be stored in a variable
print(new_list)

new_list.reverse()                  # Can't be stored in a variable
print(new_list)