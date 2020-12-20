import random

from default_twists import default_twists
from default_wishes import default_wishes
from rarity import Rarity


class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.big_orange_head = False
        self.wishes = 3

        self.wish_pool = default_wishes()
        self.twist_pool = default_twists()

        self.generate_wish_choices = lambda: self.default_generate_wish_choices(2)
        self.generate_twist_choices = lambda wish: self.default_generate_twist_choices(wish, 2)

    def default_generate_wish_choices(self, number):
        # this is slow but "perfect"
        legendary_wishes = list(filter(lambda w: w.rarity == Rarity.LEGENDARY, self.wish_pool))
        normal_wishes = list(filter(lambda w: w.rarity == Rarity.COMMON, self.wish_pool))

        wishes = []
        for i in range(number):
            new_wish = None
            while new_wish not in wishes:
                rarity_value = random.randint(1, 10)
                if rarity_value == 1:
                    new_wish = random.choice(legendary_wishes)
                else:
                    new_wish = random.choice(normal_wishes)
            wishes.append(new_wish)

        return wishes

    def default_generate_twist_choices(self, wish, number):
        # this is slow but "perfect"
        legendary_twists = list(filter(lambda w: w.rarity == Rarity.LEGENDARY, self.twist_pool))
        normal_twists = list(filter(lambda w: w.rarity == Rarity.COMMON, self.twist_pool))

        twists = []
        for i in range(number):
            new_twist = None
            while new_twist not in twists:
                if wish.rarity == Rarity.LEGENDARY:
                    new_twist = random.choice(legendary_twists)
                else:
                    new_twist = random.choice(normal_twists)
            twists.append(new_twist)

        return twists
