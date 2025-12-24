my_file = open("class_material/Prueba.txt")

print(my_file)
print(my_file.read())

one_line = my_file.readline()
print(one_line.upper())
one_line = my_file.readline()
print(one_line.rstrip())
one_line = my_file.readline()
print(one_line)

for l in my_file:
    print(f"Line reads: {l}")

all_lines = my_file.readlines()
print(all_lines)

last_line = all_lines.pop()
print(last_line)

my_file.close()