my_text = "This is Andy's text"
a = "Learning"
b = "Python"
c = "is"
d = "cool"

# upper()
result = my_text.upper()
print(result)

result = my_text[2].upper()
print(result)

# lower()
result = my_text.lower()
print(result)

# split()
result = my_text.split()
print(result)

result = my_text.split("s")
print(result)

# join()
result = " ".join([a,b,c,d])
print(result)

# find()
result = my_text.find("s")
print(result)

result = my_text.find("z")  # Difference between find and index; find returns -1 when the character isn't found and index returns an error
print(result)

# replace()
result = my_text.replace("Andy's","Armando's")
print(result)

result = my_text.replace("i","x")
print(result)