import random

word_list = ["apple", "pear", "banana", "pineapple", "orange"]

word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

if len(guess) == 1 or guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")