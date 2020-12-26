from action import wish_twist_generators

from action.Action import Action
from action.GeneratorStack import GeneratorStack
from action.action_stack import ActionStack
from action.action_tag import Tag
from action.wish_twist_generators import generate_infinite, random_wish_from_pool, random_twist_from_pool
from game_types.wish.default_wishes import default_wishes
from game_types.Dice import Dice


class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.gold_modifiers = ActionStack()

    def add_gold_instant(self, bonus):
        self.gold += self.gold_modifiers.apply(bonus, [Tag.INSTANT_GOLD])

    def sub_gold_instant(self, amount):
        self.gold -= amount


class Genie(Player):
    def __init__(self, name):
        Player.__init__(self, name)

        self.twist_count_generator_stack = ActionStack()
        # self.twist_generator = twist_generator_for_wish()

    # this doesnt allow for the same kind of modification as the wish generator, but is it needed?
    def get_twist_options_for_wish(self, wish):
        twist_count = self.twist_count_generator_stack.apply(2)
        return [x for _, x in zip(range(twist_count),
                                  generate_infinite(lambda: random_twist_from_pool(default_wishes(), wish))
                                  )
                ]


class Victim(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.gold = 0
        self.big_orange_head = False
        self.wishes = 3
        self.dice = Dice()

        # self.wish_pool = default_wishes()

        self.wish_count_generator_stack = ActionStack()

        self.wish_generator_stack = GeneratorStack()
        self.wish_generator_stack.append(
            Action(generate_infinite(lambda: random_wish_from_pool(default_wishes())), 100, []))

    def get_wish_options(self):
        wish_count = self.wish_count_generator_stack.apply(2)
        return self.wish_generator_stack.generate_n(wish_count)
