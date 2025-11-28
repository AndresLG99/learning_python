# AND
# OR
# NOT

my_bool = (4 < 5) and (5 > 6)
print(my_bool)
print("-" * 50)
print("")

my_bool = (4 < 5) and (5 == 2 + 3)
print(my_bool)
print("-" * 50)
print("")

my_bool = (55 == 55) and ("dog" == "dog")
print(my_bool)
print("-" * 50)
print("")

my_bool = (1 == 10) or (3 == 3)
print(my_bool)
print("-" * 50)
print("")

my_bool = (1 == 10) or (3 == 30)
print(my_bool)
print("-" * 50)
print("")

text = "this phrase is short"

my_bool = ("phrase" in  text) and ("python" in text)
print(my_bool)
print("-" * 50)
print("")

my_bool = not ("dog" == "doggy")
print(my_bool)
print("-" * 50)
print("")
