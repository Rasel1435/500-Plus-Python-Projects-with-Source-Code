"""
The number guessing game is a popular game among programmers. In the number guessing game, 
the program selects a random number between two numbers, and the user guesses the correct number. 
If you want to learn how to create a guessing game using Python, this article is for you. 
In this article, I will take you through a tutorial on creating a number guessing game using the Python programming language.
"""

"""
### Number Guessing Game using Python ###

To create a guessing game, we need to write a program to select a random number between 1 and 10.
To give hints to the user, we can use conditional statements to tell the user if the guessed number is smaller, 
greater than or equal to the randomly selected number.

So below is how you can write a program to create a number guessing game using Python:
"""

import random

n = random.randrange(1,10)
guess = int(input("Enter Any Number: "))

while n!= guess:
    if guess < n:
        print("Guess is too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Guess is too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("You guessed it right!!")