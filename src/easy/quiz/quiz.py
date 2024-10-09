import sys
import os
import json
from pathlib import Path


DIR_PATH = Path(__file__).parent.resolve()


def load_questions():
    questions = None
    with open(os.path.join(DIR_PATH, "questions.json"), "r") as f:
        questions = json.load(f)
    return questions


def compare_user_ans(user_ans, actual):
    return actual.lower() == user_ans.lower()


class Quiz:

    def __init__(self) -> None:
        self.questions = load_questions()
        self.correct = 0

    def start(self):
        option = input("Do you want to take the quiz? [yes/no]: ")
        is_play = compare_user_ans(option, "yes")
        if not is_play:
            sys.exit(1)
        self.ask_questions()
        self.calc_result()

    def ask_questions(self):
        for question, answer in self.questions:
            ans = input(f"{question}:\t")
            is_correct = compare_user_ans(ans, answer)
            if is_correct:
                self.correct += 1

    def calc_result(self):
        num_questions = len(self.questions)
        accuracy = (self.correct / num_questions) * 100
        print(
            f"Your accuracy is {accuracy}%. Answered {self.correct} questions correct out of {num_questions}"
        )
