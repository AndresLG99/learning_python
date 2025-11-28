my_list = ["a","b","c"]
for letter in my_list:
    num_letter = my_list.index(letter) + 1
    print(f"Letter {num_letter}: {letter}")

my_list = ["Pablo","Laura","Fede","Luis","Julia"]
for name in my_list:
    if name.startswith("L"):
        print(name)
    else:
        print("Doesn't start with 'L'")

nums = [1,2,3,4,5]
val = 0
for num in nums:
    val += num
print(val)

word = "python is great"
for letter in word:
    print(letter)

for item1,item2 in [[1,2],[3,4],[5,6]]:
    print(item1)
    print(item2)

dic = {"v1":"a","v2":"b","v3":"c"}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for item in dic.keys():
    print(item)