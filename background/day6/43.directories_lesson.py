import os
from pathlib import Path

"""
path = os.getcwd()
print(path)

os.chdir("D:\\Documents Local\\Portfolio\\learning_python\\background\\day6\\class_material\\directory_test")

file = open("test_file.txt", "w")
file.write("test file content")
file.close()

os.mkdir("D:\\Documents Local\\Portfolio\\learning_python\\background\\day6\\class_material\\test_dir")
os.makedirs("D:\\Documents Local\\Portfolio\\learning_python\\background\\day6\\class_material\\test_dir2")

new_path = "D:\\Documents Local\\Portfolio\\learning_python\\background\\day6\\class_material\\directory_test\\test_file.txt"
element = os.path.basename(new_path)
print(element)
element2 = os.path.dirname(new_path)
print(element2)
element3 = os.path.split(new_path)
print(element3)

os.rmdir("D:\\Documents Local\\Portfolio\\learning_python\\background\\day6\\class_material\\test_dir2")

other_file = open("D:\\Documents Local\\Portfolio\\learning_python\\background\\day6\\class_material\\directory_test\\test_file.txt")
print(other_file.read())
other_file.close()
"""

directory = Path("D:/Documents Local/Portfolio/learning_python/background/day6/class_material/directory_test")
file = directory / "test_file.txt"
my_file = open(file)
print(my_file.read())
my_file.close()