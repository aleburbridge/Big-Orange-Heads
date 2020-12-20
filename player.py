import random
import wish_generators

from BaseApplicationActionStack import BaseApplicationActionStack
from action import Action
from action_stack import ActionStack
from action_tag import Tag
from default_twists import default_twists
from default_wishes import default_wishes
from rarity import Rarity
from dice import Dice


class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.big_orange_head = False
        self.wishes = 3
        self.dice = Dice()
        self.gold_modifiers = ActionStack(lambda x: x)

        self.wish_pool = default_wishes()
        self.twist_pool = default_twists()

        self.wish_generator_action_stack = BaseApplicationActionStack(
            wish_generators.default_wish_generator_for_pool,
            [Action(wish_generators.generate_n_no_dupes(2), 0, [])]
        )
        self.generate_twist_choices = lambda wish: self.default_generate_twist_choices(wish, 2)
    
    def add_gold_instant(self, bonus):
        self.gold += self.gold_modifiers.apply([Tag.INSTANT_GOLD], bonus)

    def sub_gold_instant(self, amount):
        self.gold -= amount

    def default_generate_twist_choices(self, wish, number):
        # this is slow but "perfect"
        legendary_twists = list(filter(lambda w: w.rarity == Rarity.LEGENDARY, self.twist_pool))
        normal_twists = list(filter(lambda w: w.rarity == Rarity.COMMON, self.twist_pool))

        twists = []
        for i in range(number):
            while True:
                if wish.rarity == Rarity.LEGENDARY:
                    new_twist = random.choice(legendary_twists)
                else:
                    new_twist = random.choice(normal_twists)
                if new_twist not in twists:
                    twists.append(new_twist)
                    break

        return twists
