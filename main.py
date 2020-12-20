from cmdline_interface import CmdlineInterface
from game_types.Game import Game

print("sup")

game = Game(input("Enter the names of the players separated by a space \n").split(), CmdlineInterface())
game.start_game()