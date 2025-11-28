my_list = ["a","b","c"]
index = 0
for item in my_list:
    print(index, item)
    index += 1

for item in enumerate(my_list):
    print(item)

for index, item in enumerate(my_list):
    print(index, item)

for index, item in enumerate(range(50,55)):
    print(index, item)

tuples = list(enumerate(my_list))
print(tuples)
print(tuples[1][0])