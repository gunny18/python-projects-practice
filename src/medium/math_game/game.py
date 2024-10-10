import time
import random

OPERATIONS = ["+", "-", "*"]
MAX_VAL = 12
MIN_VAL = 3
MAX_QUESTIONS = 10


def check_digit(val: str):
    if val.isdigit():
        return int(val)
    return int(val)


def get_expr():
    left = random.randint(MIN_VAL, MAX_VAL)
    right = random.randint(MIN_VAL, MAX_VAL)
    operator = random.choice(OPERATIONS)
    return f"{left} {operator} {right}"


class Game:

    def __init__(self) -> None:
        pass

    def prompt_question(self):
        for i in range(MAX_QUESTIONS):
            question = get_expr()
            while True:
                ans = input(f"Q{i+1}. {question} = ")
                val = check_digit(ans)
                if val == eval(question):
                    break
                else:
                    print("wrong")

    def start(self):
        input("Start game?")
        start = time.time()
        self.prompt_question()
        end = time.time()
        print(f"Took {end-start} seconds")
