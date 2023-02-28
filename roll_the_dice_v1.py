import random
import easygui

player_one_rolls = [0, 0]
player_two_rolls = [0, 0]
player_two_rolls_add = 0
player_one_rolls_add = 0
possible_rolls = [1, 2, 3, 4, 5, 6]
roll_completed = 0

while roll_completed == 0:
    player_one_rolls[0] = random.choice(possible_rolls)
    player_one_rolls[1] = random.choice(possible_rolls)
    player_one_rolls_add = player_one_rolls[0] + player_one_rolls[1]
    player_two_rolls[0] = random.choice(possible_rolls)
    player_two_rolls[1] = random.choice(possible_rolls)
    player_two_rolls_add = player_two_rolls[0] + player_two_rolls[1]
    easygui.msgbox("player one rolled", player_one_rolls[0], "and", player_one_rolls[1], "total", player_one_rolls_add)
    easygui.msgbox("player two rolled", player_two_rolls[0], "and", player_two_rolls[1], "total", player_two_rolls_add)
    roll_completed = 1




