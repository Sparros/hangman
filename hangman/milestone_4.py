import random

class Hangman:
    word_list = ["apple", "pear", "banana", "pineapple", "orange"]

    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

        print(f"The mystery word has {self.num_letters} characters")
        print(self.word_guessed)
    
    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if not len(guess) == 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already guessed that letter.")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

hangman_game = Hangman()
hangman_game.ask_for_input()