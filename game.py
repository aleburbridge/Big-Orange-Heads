import random

import cmdline_interface
from Choice import Choice
from rarity import Rarity
from player import Player
import screen_utils


class Game:
    def __init__(self, player_names, interface):
        players = [Player(x.lower()) for x in player_names]
        self.genie = random.choice(players)
        players.remove(self.genie)
        random.shuffle(players)
        self.victims = players
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
            wishes = turn_player.generate_wish_choices()
            choices = [Choice(wish, turn_player.generate_twist_choices(wish)) for wish in wishes]
            choice = self.interface.player_choose(self, choices)
            twist = self.interface.genie_choose(self, choice.twists)

            choice.wish.action(self)
            twist.action(self)

            turn_player.wishes -= 1
            self.turn += 1
        print("GAME OVA")
