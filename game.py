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

    def get_total_gold(self):
        return sum(map(lambda x: x.gold, self.victims))

    def get_total_wishes(self):
        return sum(map(lambda x: x.wishes, self.victims))

    def increment_turn(self):
        self.turn = (self.turn + 1) % len(self.victims)

    def start_game(self):
        while self.get_total_wishes() != 0:
            turn_player = self.victims[self.turn]
            wishes = turn_player.generate_wish_choices()
            choices = [Choice(wish, turn_player.generate_twist_choices(wish)) for wish in wishes]
            choice = self.interface.player_choose(turn_player, choices)
            self.interface.genie_choose(turn_player, choice.twists)
