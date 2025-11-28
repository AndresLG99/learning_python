coins = 5
while coins > 0:
    print(f"I have {coins} coins.")
    coins -= 1
else:
    print("No coins left.")

answer = "y"
while answer == "y":
    answer = input("Do you want to continue? [Y/N] ").lower()
else:
    print("Thank you for playing.")

# PASS
answer = "y"
while answer == "y":
    pass
print("HELLO")

# BREAK
name = input("What is your name? ")
for letter in name:
    if letter == "r":
        break
    print(letter)

# CONTINUE
name = input("What is your name? ")
for letter in name:
    if letter == "r":
        continue
    print(letter)