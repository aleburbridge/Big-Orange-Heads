import screen_utils
from Choice import Choice
from Twist import Twist
from player import Player


class CmdlineInterface:

    def print_twists(self, twists):
        for idx, twist in enumerate(twists):
            print(chr(ord('a') + idx) + ". " + twist.description)

    def player_choose(self, player: Player, choices: list[Choice]):
        screen_utils.create_suspense(5)

        print("Wisher: " + player.name.capitalize() + " (" + str(player.wishes) + " wishes left)")
        print("Gold: " + str(player.gold))

        print("~~ WISHES ~~\n")

        for c_idx, choice in enumerate(choices):
            print(str(c_idx) + ". " + choice.wish.description)
            screen_utils.print_line_break()
            for t_idx, twist in enumerate(choice.twists):
                print(chr(ord('a') + t_idx) + ". " + twist.description)
            print()

        while True:
            response = int(input("\n\n"))

            if response in range(len(choices)):
                return choices[response]

            print("that wasnt a valid response dummy...")


    def genie_choose(self, player: Player, twists: list[Twist]):
        print("GENIE! CHOOSE YOUR TWIST!")
        for idx, twist in enumerate(twists):
            print(str(idx) + ". " + twist.description)

        while True:
            response = int(input("\n\n"))

            if response in range(len(twists)):
                return twists[response]