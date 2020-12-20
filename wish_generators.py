from rarity import Rarity
import random


def default_wish_generator_for_pool(pool):
    def default_generate_wish_choice():
        rarity_value = random.randint(1, 10)
        if rarity_value == 1:
            legendary_wishes = list(filter(lambda w: w.rarity == Rarity.LEGENDARY, pool))
            new_wish = random.choice(legendary_wishes)
        else:
            normal_wishes = list(filter(lambda w: w.rarity == Rarity.COMMON, pool))
            new_wish = random.choice(normal_wishes)

        return new_wish

    return default_generate_wish_choice


def generate_n_no_dupes(n):
    def generator_n(base, wishes):
        for i in range(n):
            while True:
                new_wish = base()

                if new_wish not in wishes:
                    wishes.append(new_wish)
                    break
        return wishes

    return generator_n
