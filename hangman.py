import random

class Hangman:

    """
    Initializes the Hangman game with a random word from the provided list.
    Initializes variables to track guessed letters, remaining lives, and the mystery word.
    """
    def __init__(self, word_list, num_lives = 6):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

        print(f"The mystery word has {self.num_letters} characters")
        print(self.word_guessed)
    
    """
    Checks the guessed letter against the mystery word.
    Updates the guessed word and remaining unique letters accordingly.
    Prints feedback to the player based on the correctness of the guess.
    """
    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            print(self.word_guessed)
            print(self.display_hangman())
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(self.display_hangman())
            print(f"You have {self.num_lives} lives left.")
            
    """
    Prompts the user to guess a letter.
    Validates the input and ensures it's a valid single alphabetical character.
    Calls check_guess to process the guess and update the game state.
    """
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already guessed that letter.")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break
    
    """
    Displays the hangman stage based on the remaining lives.
    Returns ASCII art representing the hangman's current state.
    """
    def display_hangman(self):
        stages = [
            """
            ------
            |    |
            |
            |
            |
            |
            """,
            """
            ------
            |    |
            |    O
            |
            |
            |
            """,
            """
            ------
            |    |
            |    O
            |    |
            |
            |
            """,
            """
            ------
            |    |
            |    O
            |   /|
            |
            |
            """,
            """
            ------
            |    |
            |    O
            |   /|\\
            |
            |
            """,
            """
            ------
            |    |
            |    O
            |   /|\\
            |   /
            |
            """,
            """
            ------
            |    |
            |    O
            |   /|\\
            |   / \\
            |
            """
        ]
        if self.num_lives > 0:
            return stages[6 - self.num_lives]
        else:
            # Display final stage when the player loses
            return stages[-1]

    """
    Main game loop where the player plays the Hangman game.
    Continues until the player wins, loses, or chooses to quit.
    """
    def play_game(self):
        while True:
            if self.num_lives == 0:
                print("You lost! The word was:", self.word)
                break
            elif self.num_lives > 0 and self.num_letters > 0:
                self.ask_for_input()
            elif self.num_lives > 0 and self.num_letters == 0:
                print("You won!")
                print("The word was:", self.word)
                break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    game = Hangman(word_list)
    game.play_game()