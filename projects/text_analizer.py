# Asks user to input a text
# Asks user to input 3 letters
# Code should output how many times the 3 inputed letters appear in the text
# Code should output how many words are there in the text
# Code should output what's the first and last letter of the text
# Code should output the same text reversed (words)
# Code should output if the word "Python" appears in the text

# USER INPUTS
text = input("Please enter a text: ")
l1 = input("Please enter a letter: ")
l2 = input("Please enter a second letter: ")
l3 = input("Please enter a third letter: ")

# COUNT APPEARENCES
count_l1 = text.lower().count(l1.lower())
count_l2 = text.lower().count(l2.lower())
count_l3 = text.lower().count(l3.lower())

# COUNT WORDS
word_list = text.split()
count_words = len(word_list)

# FIRST AND LAST LETTERS
first_letter = text[0]
last_letter = text[-1]

# TEXT REVERSED
rev_word_list = word_list[::-1]
rev_text = " ".join(rev_word_list)

# PYTHON?
python_appear = "Python".lower() in text.lower()
answer = {True:"Yes", False:"No"}

# PRINT OUTPUTS
print(f"\nThe letter '{l1}' appears {count_l1} times")
print(f"The letter '{l2}' appears {count_l2} times")
print(f"The letter '{l3}' appears {count_l3} times")
print(f"\nThere's {count_words} words in the text")
print(f"\nThe first letter in the text is '{first_letter}' and the last letter is '{last_letter}'")
print(f"\nThe reversed text is\n'{rev_text}'")
print(f"\nThe word 'Python' appears in the text?\n{answer[python_appear]}")