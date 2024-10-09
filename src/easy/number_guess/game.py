import sys
import random


def extract_digit(val: str):
    if val.isdigit():
        return int(val)


def get_random_number(upper_bound: int):
    return random.randint(1, upper_bound)


class NumberGame:
    def __init__(self):
        self._guesses = 0
        self._number = 0

    def start(self):
        user_ans = input("Enter a upper bound number [>0]: ")
        val = extract_digit(user_ans)
        if not val:
            print("Not a valid digit")
            sys.exit(1)
        self._number = get_random_number(val)
        self.begin_game()
        self.show_result()

    def begin_game(self):
        while True:
            guess = input("Guess the number: ")
            self._guesses += 1
            val = extract_digit(guess)
            if not val:
                print("Enter a valid digit!!")
                continue
            if val == self._number:
                print("You got it.")
                break
            elif val > self._number:
                print("Answer is higher than actual value. Guess lower")
            else:
                print("Answer is lower than actual value. Guess higher")

    def show_result(self):
        print(f"Got it in {self._guesses} guesses")
