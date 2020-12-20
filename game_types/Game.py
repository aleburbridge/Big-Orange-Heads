import random

from game_types.Choice import Choice
from game_types.Player import Genie, Victim


class Game:
    def __init__(self, player_names, interface):
        genie_name = random.choice(player_names)
        self.genie = Genie(genie_name.lower())

        player_names.remove(genie_name)

        self.victims = [Victim(n.lower()) for n in player_names]
        random.shuffle(self.victims)
        self.turn = 0
        self.interface = interface

        self.human_items = []

    def active_player(self):
        return self.victims[self.turn % len(self.victims)]

    def get_total_gold(self):
        return sum(map(lambda x: x.gold, self.victims))

    def get_total_wishes(self):
        return sum(map(lambda x: x.wishes, self.victims))

    def start_game(self):
        self.interface.display_genie_roll(self.victims, self.genie)
        while self.get_total_wishes() != 0:
            turn_player = self.active_player()
            wishes = turn_player.wish_generator_action_stack.apply(turn_player.wish_pool)
            choices = [Choice(wish, self.genie.twist_generator_action_stack.apply(self.genie.twist_pool, wish))
                       for wish in wishes]
            choice = self.interface.player_choose(self, choices)
            twist = self.interface.genie_choose(self, choice.twists)

            choice.wish.action(self)
            twist.action(self)

            turn_player.wishes -= 1
            self.turn += 1
        print("GAME OVA")
