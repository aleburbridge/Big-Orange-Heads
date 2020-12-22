import random


class Dice:
    def __init__(self):
        pass
    
    # TODO: make this a lambda when stack is here
    def perform_d12_roll(self, game):
        result = random.randint(1, 12)
        game.interface.display_dice_roll(12, result, 12)
        return result