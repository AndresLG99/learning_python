from random import shuffle

# Initial list
sticks = ["-","--","---","----"]

# Shuffle sticks
def shuffle_list(lst):
    shuffle(lst)
    return lst

# Ask for a number
def try_luck():

    attempt = ""

    while attempt not in ["1","2","3","4"]:
        attempt = input("Choose a number between 1-4: ")
    return int(attempt)

# Check attempt
def check_attempt(lst, attempt):

    if lst[attempt - 1] == "-":
        print("Do the dishes!")
    else:
        print("Saved!")

    print(f"Your stick is {lst[attempt - 1]}")

shuffled_sticks = shuffle_list(sticks)
selection = try_luck()
check_attempt(shuffled_sticks, selection)