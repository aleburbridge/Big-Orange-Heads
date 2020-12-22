from game_types.Rarity import Rarity
import random


def default_wish_generator_for_pool(pool):
    def default_generate_wish_choice(filter_wishes):
        rarity_value = random.randint(2, 2)
        if rarity_value == 1:
            legendary_wishes = list(filter(lambda w: w.rarity == Rarity.LEGENDARY and w not in filter_wishes, pool))
            new_wish = random.choice(legendary_wishes)
        else:
            normal_wishes = list(filter(lambda w: w.rarity == Rarity.COMMON and w not in filter_wishes, pool))
            new_wish = random.choice(normal_wishes)

        return new_wish

    return default_generate_wish_choice


def default_twist_generator_for_pool(pool, wish):
    def default_generate_twist_for_wish(filter_twists):
        if wish.rarity == Rarity.LEGENDARY:
            legendary_twists = list(filter(lambda w: w.rarity == Rarity.LEGENDARY and w not in filter_twists, pool))
            new_twist = random.choice(legendary_twists)
        else:
            normal_twists = list(filter(lambda w: w.rarity == Rarity.COMMON and w not in filter_twists, pool))
            new_twist = random.choice(normal_twists)

        return new_twist

    return default_generate_twist_for_wish


def generate_n_no_dupes(n):
    def generator_n(base, objs):
        for _ in range(n):
            new_obj = base(objs)
            objs.append(new_obj)
        return objs

    return generator_n
