min_val = min(58,96,72,64,35)
print(min_val)

max_val = max(58,96,72,64,35)
print(max_val)

my_list = [58,96,72,64,35]
print(f"The lowest value is {min(my_list)}")
print(f"The highest value is {max(my_list)}")

names = ["Juan","Pablo","Alicia","Carlos"]
print(min(names))

name = "Carlos"
print(min(name))            # Caps sensitive

dic = {"v1":45,"v2":11}
print(min(dic))             # Key

dic = {"v1":45,"v2":11}
print(min(dic.values()))    # Values