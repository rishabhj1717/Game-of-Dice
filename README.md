# Game-of-Dice
A simple game of dice implemented in python.

## This has been tested on python 3.10.6
To download and install relevant python version, please check https://www.python.org/downloads/

## Running the program

There are two approaches that have been added to this repository.

Approach 1 - `dice_game.py` 
Here we rank the player when the player has reached the target score. To run this approach, execute the following command

```
python dice_game.py <number_of_players> <target_score>

eg:

python dice_game.py 6 40
```

Approach 2 - `dice_game_score_approach.py`
Here we rank the player based on the score by the player. If a player finished the game later, but with a higher score, that player would be ranked higher.

```
python dice_game_score_approach.py <number_of_players> <target_score>

eg:

python dice_game_score_approach.py 6 40
```
