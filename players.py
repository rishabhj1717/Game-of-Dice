import random

class Player:
    def __init__(self, name) -> None:
        self.name = f"Player-{name}"
        self.score = 0
        self.rank = 0
        self.skip_next = False
        # keep a track of the number on dice during each round.
        self.last_roll_dice = 0


    def toggle_skip(self, bool):
        self.skip_next = bool

    def update_last_roll_dice(self, new_roll):
        self.toggle_skip(all([new_roll==1,self.last_roll_dice==1]))
        self.last_roll_dice = new_roll

    def update_rank(self, rank):
        self.rank=rank

    def roll_dice(self) -> int:
        #Generate a random number from 1 to 6, just like the dice.
        return random.randint(1,6)

    def update_score(self, score) -> None:
        self.score += score
