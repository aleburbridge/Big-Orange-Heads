class GeneratorStack:
    def __init__(self):
        self._generators = []

    def append(self, generator):
        self._generators.append(generator)
        self._generators.sort(key=lambda a: a.priority)

    def generator_sum(self, tags=None):
        if tags is None:
            tags = []
        filtered_actions = filter(lambda x: len(x.tags) == 0 or any(tag in tags for tag in x.tags), self._generators)

        for action in filtered_actions:
            yield from action.fn

    def generate_n(self, n, tags=None):
        # generate up to n elements from the generator
        return [x for _, x in zip(range(n), self.generator_sum(tags))]


if __name__ == "__main__":
    import random

    from action.Action import Action
    from game_types.Rarity import Rarity
    from game_types.wish.default_wishes import default_wishes

    def default_generate_wish_choice(pool):
        rarity_value = random.randint(1, 2)
        if rarity_value == 1:
            legendary_wishes = list(filter(lambda w: w.rarity == Rarity.LEGENDARY, pool))
            new_wish = random.choice(legendary_wishes)
        else:
            normal_wishes = list(filter(lambda w: w.rarity == Rarity.COMMON, pool))
            new_wish = random.choice(normal_wishes)

        yield new_wish

    stack = GeneratorStack()
    stack.append(Action(default_generate_wish_choice(default_wishes()), 100, []))
    print(stack.generate_n(1)[0].description)


