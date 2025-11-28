# if
# elif
# else

if 10 > 9:
    print("Correct")

if True:
    print("Correct")

x = True
if x:
    print("Correct")

if 5 == 2:
    print("Correct")
else:
    print("Incorrect")

pet = "rabbit"
if pet == "cat":
    print("You have a cat")
elif pet == "dog":
    print("You have a dog")
elif pet == "fish":
    print("You have a fish")
else:
    print("I don't know what is your pet")

age = 16
grade = 9
if age < 18:
    print("Underage")
    if grade > 7:
        print("Pass")
    else:
        print("Fail")
else:
    print("Adult")