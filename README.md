# Projects Repository

---

## beer_name_creator  
- Program that asks the user two questions of your choosing  
- Show in the console both answers as part of a text "The name of the beer is (Beer Name)"  
- The beer name has to be in between double quotations and in a second line of text  

---
  
## commission_calculator  
- Calculate commission to be paid to employees based on their sales  
- Commission is 13% of the total $$$ sold  
- Code should ask for the name of the employee and how much $$$ have they sold  
- Code should output a phrase stating the employee name and how much $$$ they'll get paid  

---

## text_analyzer  
- Asks user to input a text  
- Asks user to input 3 letters  
- Code should output how many times the 3 inputted letters appear in the text  
- Code should output how many words are there in the text  
- Code should output what's the first and last letter of the text  
- Code should output the same text reversed (words)  
- Code should output if the word "Python" appears in the text  

---

## guessing_game
- Ask for user's name
- Gives an intro to the game
- Starts with 8 attempts
- Range between 1 and 100
- Select a random number in the range
- Asks user to input a number in the range
- Handles numbers out of range, doesn't affect remaining attempts
- If the inputted number is lower than the chosen number
    - Update range
    - Print message stating the inputted number is lower
- If the inputted number is higher than the chosen number
    - Update range
    - Print message stating the inputted number is higher
- If the inputted number is correct
    - Print winning message
    - Attempts taken
- Loop until user wins or attempts are equal to 0

---

## hangman_game
- Ask for user's name
- Gives an intro to the game
- Starts with 6 lives
- List of words to choose from
- Code should choose a secret word from list of words
- Code should output the number of letters hidden as dashes
- Asks user to input a letter
- If the inputted letter is in the word
  - Code will replace the dashes with that letter
  - Print hidden word with uncovered letters
- If the inputted letter is not in the word
  - Code will take out a live
  - Print how many lives are left
- If user is out of lives before guessing the hidden word
  - GAME OVER
- If user guesses correctly all the letters in the hidden word
  - User wins
- Code shouldn't take out lives if user enters a repeated letter
- Code shouldn't take out lives if user enters an invalid character

---