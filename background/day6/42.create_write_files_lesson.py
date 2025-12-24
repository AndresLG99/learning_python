file = open("class_material/Prueba.txt", "a") # "w/a" | to create new files, use a new file name
file.write("""Newer text
Using mode 'a'
""")

# file.writelines(["New Text","Hello","World"]) # All items of the list are written together

file.close()