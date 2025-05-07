import random

class Word():
    def __init__(self):
        self.word = self._get_random_word()
        self.guessed = False
        self.guesses = []
        self.guesses_map = []

    def _get_random_word(self):
        with open('data/valid_solutions.csv', 'r') as file:
            words = file.readlines()

        return random.choice(words).strip()