import screen_utils
from Choice import Choice
from player import Player


class CmdlineInterface:
    def player_choose(self, player: Player, choices: list[Choice]):
        print("hi")
        screen_utils.create_suspense(5)

        print("Wisher: " + player.name.capitalize() + " (" + str(player.wishes) + " wishes left)")
        print("Gold: " + str(player.gold))

        print("~~ WISHES ~~\n")

        for choice in choices:
            print(choice.wish.description)
            screen_utils.print_line_break()
            for idx, twist in enumerate(choice.twist):
                print(chr(ord('a') + idx) + ". " + twist.description)
            print()

        while True:
            response = int(input("\n\n"))

            if response in range(len(choices)):
                return choices[response]

            print("that wasnt a valid response dummy...")
