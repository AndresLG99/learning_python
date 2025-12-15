# Ask for user's name
# Gives an intro to the game
# Starts with 6 lives
# List of words to choose from
# Code should choose a secret word from list of words
# Code should output the number of letters hidden as dashes
# Asks user to input a letter
# If the inputted letter is in the word
#   - Code will replace the dashes with that letter
#   - Print hidden word with uncovered letters
# If the inputted letter is not in the word
#   - Code will take out a live
#   - Print how many lives are left
# If user is out of lives before guessing the hidden word
#   - GAME OVER
# If user guesses correctly all the letters in the hidden word
#   - User wins
# Code shouldn't take out lives if user enters a repeated letter
# Code shouldn't take out lives if user enters an invalid character

# IMPORTS
from random import choice

# VARIABLES
lives = 6
words = ["python","galaxy","algorithm","glacier","symphony","lantern","encryption","horizon","quantum","avalanche"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
used_letters = []
correct_guesses = []
game_over = False

# FUNCTIONS
def name():
    n = input("Enter your name: ").capitalize()
    return n

def intro(n):
    print(f"Welcome to the Hangman Game {n}!")
    print("The goal is to uncover the secret word before you run out of lives.")
    print("I'll choose a random word to guess.")
    print("I'll show you the hidden letters by a dash.")
    print("The amount of dashes matches the amount of letters the secret word has.")
    print("If you guess correctly I'll show you the letter you chose in the respective space.")
    print("If you guess incorrectly I'll take out a live.")
    print("For starters, you'll have 6 lives.")

def start():
    answer = input("Would you like to play? (y/n): ")
    while answer not in  ["y","n"]:
        answer = input("Enter a valid option (y/n): ")
    if answer == "y":
        return False
    else:
        print("See you next time!")
        return True

def show_hidden_word(word,ul):
    print("Hidden word: ")
    for i in word:
        if i in set(ul):
            print(i,end="")
        else:
            print("-",end="")

def show_lives_left(lv):
    print(f"{lv} lives left")

def show_used_letters(ul):
    print("Used letters: ",end="")
    for i in ul:
        print(f"{i}",end="/")

def choose_letter(ul):
    letter = input("Enter a letter: ")
    while letter.lower() not in alphabet:
        letter = input("Enter a valid letter: ")
    while letter.lower() in ul:
        letter = input("Enter a letter that hasn't been used already: ")
    return letter.lower()

def validate_guess(guess,sw,lv,ul,cl):
    if guess in sw:
        ul.append(guess)
        cl.append(guess)
    else:
        lv -= 1
        ul.append(guess)
    return guess, lv, ul

def validate_game(lv,sw,cl):
    global game_over
    if (lv > 0) and (len(cl) != len(sw)):
        game_over = False
    elif (lv > 0) and (len(cl) == len(sw)):
        print("Congrats, you won!")
        print(f"The secret word was: {sw}")
        game_over = True
    elif (lv <= 0) and (len(cl) != len(sw)):
        print("Sorry, you lost!")
        print(f"The secret word was: {sw}")
        game_over = True
    return game_over

# GAME
# Intro
user = name()
print()
intro(user)
print("\n" + "*" * 100)

# Want to play?
game_over = start()
print("\n" + "*" * 100)

# Choose secret word
secret_word = choice(words)

while not game_over:
    show_hidden_word(secret_word,used_letters)
    print()
    show_lives_left(lives)
    show_used_letters(used_letters)
    print("\n" + "*" * 100)

    # User choose letter
    chosen_letter = choose_letter(used_letters)
    print()

    # Check valid letter
    guess, lives, used_letters = validate_guess(chosen_letter,secret_word,lives,used_letters,correct_guesses)

    # Validate if game over
    validate_game(lives,secret_word,correct_guesses)