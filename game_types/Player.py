from action import wish_twist_generators

from action.BaseApplicationActionStack import BaseApplicationActionStack
from action.Action import Action
from action.action_stack import ActionStack
from action.action_tag import Tag
from game_types.twist.default_twists import default_twists
from game_types.wish.default_wishes import default_wishes
from game_types.Dice import Dice


class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.gold_modifiers = ActionStack(lambda x: x)

    def add_gold_instant(self, bonus):
        self.gold += self.gold_modifiers.apply([Tag.INSTANT_GOLD], bonus)

    def sub_gold_instant(self, amount):
        self.gold -= amount


class Genie(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.twist_pool = default_twists()
        self.twist_generator_action_stack = BaseApplicationActionStack(
            wish_twist_generators.default_twist_generator_for_pool,
            [Action(wish_twist_generators.generate_n_no_dupes(2), 0, [])]
        )


class Victim(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.gold = 0
        self.big_orange_head = False
        self.wishes = 3
        self.dice = Dice()

        self.wish_pool = default_wishes()

        self.wish_generator_action_stack = BaseApplicationActionStack(
            wish_twist_generators.default_wish_generator_for_pool,
            [Action(wish_twist_generators.generate_n_no_dupes(2), 0, [])]
        )
