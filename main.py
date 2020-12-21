from cmdline_interface import CmdlineInterface
from game_types.Game import Game
from testing.fast_cmdline_interface import FastCmdlineInterface

print("sup")

game = Game(input("Enter the names of the players separated by a space \n").split(), FastCmdlineInterface())
game.start_game()