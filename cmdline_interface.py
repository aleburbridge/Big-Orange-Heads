import random
import time

from game_types.Choice import Choice
from game_types.twist.Twist import Twist
from game_types.Game import Game


class CmdlineInterface:

    def print_twists(self, twists):
        for idx, twist in enumerate(twists):
            print(chr(ord('a') + idx) + ". " + twist.description)

    def player_choose(self, game: Game, choices: list[Choice]):
        self.create_suspense(5)

        active_player = game.active_player()
        print("\n")
        print("Wisher: " + active_player.name.capitalize() + " (" + str(active_player.wishes) + " wishes left)")
        print("Gold: " + str(active_player.gold))

        print("~~ WISHES ~~\n")

        for c_idx, choice in enumerate(choices):
            print(str(c_idx) + ". " + choice.wish.description)
            self.print_line_break()
            for t_idx, twist in enumerate(choice.twists):
                print(chr(ord('a') + t_idx) + ". " + twist.description)
            print()

        while True:
            response = int(input("\n"))

            if response in range(len(choices)):
                print("\n")
                return choices[response]

            print("that wasnt a valid response dummy...")


    def genie_choose(self, game: Game, twists: list[Twist]):
        print("GENIE! CHOOSE YOUR TWIST!")
        for idx, twist in enumerate(twists):
            print(str(idx) + ". " + twist.description)

        while True:
            response = int(input("\n\n"))

            if response in range(len(twists)):
                return twists[response]
    
    def create_suspense(self, suspense_amount):
        # for x in range(1, suspense_amount):
        #     b = "Supsense" + "." * x
        #     print(b, end="\r")
        #     time.sleep(1)
        pass

    def display_dice_roll(self, num_rolls, result, dice_size):
        for x in range(1, num_rolls):
            print(str(random.randint(1,dice_size)) + (" " * 5), end="\r")
            time.sleep(x / num_rolls)
        print(str(result) + (" " * 5))
        time.sleep(1)

    def display_genie_roll(self, victims, genie):
        all_players = victims + [genie]
        print("The genie is ...")
        for i in range(len(all_players) * 5):
            print(random.choice(all_players).name + (" " * 10), end="\r")
            time.sleep(i / (len(all_players) * 5))
        print(genie.name + "!" + (" " * 10))
        time.sleep(2)
        print("\n")

    def print_line_break(self):
        print("--------------------------------------------------------------------")