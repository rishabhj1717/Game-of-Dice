import random
import sys
from players import Player


class GameOfDice:
    def __init__(self, num_players, target_score) -> None:
        self.gamers = []
        self.rank = 1
        self.num_players = num_players
        self.target_score = target_score
        self.ranking = {}
        self.create_players()
        random.shuffle(self.gamers)

    def create_players(self) -> None:
        '''
        Dummy function to create players from 1 to self.num_players
        '''
        for i in range(self.num_players):
            self.gamers.append(Player(i+1))

    def dice_game(self, current_player) -> None:
        '''
        This function updates the score for each player.

        Following Assumptions have been made:
         - If a players score exceeds the target score, their game has ended, and ranks is assigned to the player.
         In this case, the player is excluded from the further steps.
         - Players ranking is decided on when they exit the game and is updated based on the score.
            eg: A player with score 12 would have a higher ranking than a player with score 10 even if the player has exited earlier.

        '''

        roll_value = current_player.roll_dice()
        print("\n", "*"*40,
              f"{current_player.name} rolls the dice and gets {roll_value}.", "*"*40, sep="\n", end="\n\n")

        roll_score = current_player.score + roll_value
        current_player.update_last_roll_dice(roll_value)
        current_player.update_score(roll_value)

        if (roll_score >= self.target_score):
            current_player.update_rank(self.rank)#once rank for player is updated, considered to be out of the game
            self.ranking[current_player.name] = current_player.score
            print(
                f"\n\n{current_player.name} Has completed the game and is awarded the rank {self.rank}\n\n")
            self.rank += 1

        else:
            if (roll_value == 6):
                print(
                    f"{current_player.name} has got a 6! Player will role the dice again.", end="\n")
                self.dice_game(current_player)

        return

    def play_game(self):
        '''
        In this function, we are calling the function dice_game till all players have finished the game.
        We skip function call to dice_game if:
         - there have been consecutive 1s for the player
         - if the players rank has been updated.

        '''
        user_input = ''
        while (self.rank <= self.num_players):
            for gamer in self.gamers:
                # when we skip_next is true, we skip the gamers turn
                if (gamer.skip_next):
                    print(
                        f"{gamer.name} Your turn has been skipped as a penalty for getting consecutive 1s")
                    gamer.update_last_roll_dice(0)
                    continue
                # gamer is ranked and has completed the game. We can skip the gamer
                if (self.ranking.get(gamer.name)):
                    continue

                #We do not continue further if user does not enter 'r'
                while (user_input != 'r'):
                    user_input = input(
                        f"{gamer.name} , it is your turn (press \'r\' to roll the dice).")

                self.dice_game(gamer)
                user_input = ''

            self.display_score()

        print("\nGame Over!")
        print("Final Rankings:")
        sorted_ranking = sorted(self.ranking.items(), key=lambda x: x[1], reverse=True)
        for rank, (player_name, points) in enumerate(sorted_ranking, start=1):
            print(f"Rank {rank}: {player_name} - {points} points")


    def display_score(self):
        print("\nNOTE: Rank here is calculated as per the score.")
        sorted_gamers = sorted(self.gamers, key=lambda x: x.score, reverse=True)
        for ind,gamer in enumerate(sorted_gamers):
            print(f"Rank {ind+1}: {gamer.name} - {gamer.score} points")



def main():
    game_of_dice = GameOfDice(int(sys.argv[1]), int(sys.argv[2]))
    game_of_dice.play_game()

main()
