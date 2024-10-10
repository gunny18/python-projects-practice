import random


def roll(min_val=1, max_val=6):
    return random.randint(min_val, max_val)


def check_digit(val: str):
    if val.isdigit():
        return int(val)


class Game:

    def __init__(self, max_score=20) -> None:
        self.player_scores = None
        self.max_score = max_score

    def init_players(self, num_players):
        self.player_scores = [0 for _ in range(num_players)]

    def prompt_players(self):
        while True:
            players = input("Enter number of players[2 - 4]: ")
            val = check_digit(players)
            if val is None or not (2 <= val <= 4):
                print("Invalid!")
            else:
                self.init_players(val)
                break

    def will_not_roll(self):
        val = input("Do you want to roll [y]?: ")
        return val.lower() != "y"

    def calc_winner(self):
        winning_idx = self.player_scores.index(max(self.player_scores))
        print(
            f"Player {winning_idx+1} wins with score of {self.player_scores[winning_idx]}"
        )

    def begin_game(self):
        while max(self.player_scores) < self.max_score:
            for player_idx in range(len(self.player_scores)):
                print(
                    f"Player {player_idx+1} has the dice. Your total score is {self.player_scores[player_idx]}"
                )
                chance_score = 0
                while True:
                    if self.will_not_roll():
                        break
                    roll_val = roll()
                    print(f"Rolled {roll_val}")
                    if roll_val == 1:
                        self.player_scores[player_idx] = 0
                        chance_score = 0
                        break
                    else:
                        chance_score += roll_val
                self.player_scores[player_idx] += chance_score
                print("Total score:", self.player_scores[player_idx])

    def start(self):
        self.prompt_players()
        self.begin_game()
        self.calc_winner()
