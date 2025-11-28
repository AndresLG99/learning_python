# Ask for user's name
# Gives an intro to the game
# Starts with 8 attempts
# Range between 1 and 100
# Select a random number in the range
# Asks user to input a number in the range
# Handles numbers out of range, doesn't affect remaining attempts
# If the inputed number is lower than the chosen number
#   - Update range
#   - Print message stating the inputed number is lower
# If the inputed number is higher than the chosen number
#   - Update range
#   - Print message stating the inputed number is higher
# If the inputed number is correct
#   - Print winning message
#   - Attempts taken
# Loop until user wins or attempts are equal to 0

# IMPORTS
from random import choice

# INITIAL VARIABLES
lives = 8
initial_num = 1
final_num = 100
initial_range = range(initial_num,final_num + 1)
secret_num = choice(initial_range)

# INTRO
user_name = input("Hi! What is your name? ").capitalize()
print()
print(f"Hi {user_name}. Welcome to the Guessing Game!")
print()
print(f"This game is about guessing a number between {initial_num} and {final_num}.")
print()
print("If you guess correctly, I'll tell you how many attempts it took you.")
print("If you guess incorrectly, I'll give you a hint and adjust the range for you.")
print("If you select a not valid option, I'll ask you to try again and won't take any lives from you.")

# GAME
playing = input("Would you like to play? (y/n) ").lower()
while (playing != "y") and (playing != "n"):
    playing = input("Would you like to play? (y/n) ").lower()
if playing == "n":
    print("Okay! See you later!")

while lives > 0 and playing != "n":
    print()
    user_num = int(input(f"Choose a number between {initial_num} and {final_num}: "))
    while user_num not in initial_range:
        user_num = int(input(f"Choose a number between {initial_num} and {final_num}: "))
    if user_num < secret_num:
        print()
        print("Your guess is too low.")
        lives -= 1
        print(f"You have {lives} lives left.")
        initial_num = user_num + 1
        initial_range = range(initial_num,final_num + 1)
    elif user_num > secret_num:
        print()
        print("Your guess is too high.")
        lives -= 1
        print(f"You have {lives} lives left.")
        final_num = user_num - 1
        initial_range = range(initial_num, final_num + 1)
    else:
        print("You win!")
        print(f"It took you {(8 - lives) + 1} attempts.")
        break
if lives == 0:
    print()
    print("You lost!")
    print(f"The secret number was {secret_num}.")
    print("Thank you for playing!")