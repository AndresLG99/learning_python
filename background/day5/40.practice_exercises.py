# EXERCISE 1
# Create a function called return_distinct() that receives 3 integers as parameters.
# If the sum of the 3 numbers is greater than 15, it should return the largest number.
# If the sum of the 3 numbers is less than 10, it should return the smallest number.
# If the sum of the 3 numbers is between 10 and 15 (inclusive), it should return the number with the intermediate value.

# EXERCISE 2
# Write a function that receives any word as a parameter, and returns all its unique letters (without repetition) but in alphabetical order.
# For example:
# If we pass the word "entretenido" to this function, it should return ['d', 'e', 'i', 'n', 'o', 'r', 't']

# EXERCISE 3
# Write a function that requires an indefinite number of arguments.
# What this function will do is return True if at any point the number zero has been entered repeated two consecutive times.
# For example:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

# EXERCISE 4
# Write a function called count_prime() that requires a single numeric argument.
# This function will display on screen all the prime numbers existing in the range from zero up to that number inclusive, and will return the count of prime numbers it found.
# Clarification:
# By convention, 0 and 1 are not considered prime numbers.

# 1
def return_distinct(n1, n2, n3):
    x = n1 + n2 + n3
    lst = [n1, n2, n3]

    if x > 15:
        return max(lst)
    elif x < 10:
        return min(lst)
    else:
        lst.sort()
        return lst[1]

# 2
def unique_letters(word):
    lst = []
    for letter in word:
        if letter not in lst:
            lst.append(letter)
        else:
            pass
    lst.sort()
    return lst

# 3
def zero_repeat(*args):
    for i,n in enumerate(args):
        if args[i] == 0 and args[i - 1] == 0:
            return True
        else:
            pass
    return False

# 4
def count_prime(num):
    primes = [2]
    iteration = 3
    if num < 2:
        return 0

    while iteration <= num:
        for n in range(3, iteration, 2):
            if iteration % n == 0:
                iteration += 2
                break
        else:
            primes.append(iteration)
            iteration += 2
    print(primes)
    return len(primes)
