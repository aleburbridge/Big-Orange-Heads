from game_types.Rarity import Rarity
import random


def random_wish_from_pool(pool):
    rarity_value = random.randint(1, 2)
    if rarity_value == 1:
        legendary_wishes = list(filter(lambda w: w.rarity == Rarity.LEGENDARY, pool))
        new_wish = random.choice(legendary_wishes)
    else:
        normal_wishes = list(filter(lambda w: w.rarity == Rarity.COMMON, pool))
        new_wish = random.choice(normal_wishes)

    return new_wish


def random_twist_from_pool(pool, wish):
    if wish.rarity == Rarity.LEGENDARY:
        legendary_twists = list(filter(lambda w: w.rarity == Rarity.LEGENDARY, pool))
        new_twist = random.choice(legendary_twists)
    else:
        normal_twists = list(filter(lambda w: w.rarity == Rarity.COMMON, pool))
        new_twist = random.choice(normal_twists)

    return new_twist


def generate_n(fn, n):
    for _ in range(n):
        yield fn()


def generate_infinite(fn):
    while True:
        yield fn()


if __name__ == "__main__":
    import itertools

    from game_types.wish.default_wishes import default_wishes

    # print(list(itertools.islice(itertools.cycle('ab'), 5)))

    # print(list(generate_n(wish_choice_generator, 5)))
