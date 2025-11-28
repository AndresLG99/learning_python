word = "python"
my_list = []
for letter in word:
    my_list.append(letter)
print(my_list)

my_list = [x for x in "python"]
print(my_list)

my_list = [n for n in range(0,21,2)]
print(my_list)

my_list = [n / 2 for n in range(0,21,2)]
print(my_list)

my_list = [n for n in range(0,21,2) if n * 2 > 10]
print(my_list)

my_list = [n if n * 2 > 10 else "no" for n in range(0,21,2)]
print(my_list)

feet = [10,20,30,40,50]
meters = [n / 3.281 for n in feet]
print(meters)