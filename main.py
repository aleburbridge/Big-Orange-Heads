from cmdline_interface import CmdlineInterface
from game import Game

print("sup")

game = Game(input("Enter the names of the players separated by a space \n").split(), CmdlineInterface())
game.start_game()