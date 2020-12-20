import actions
from Wish import Wish, Tag
from rarity import Rarity


def default_wishes():
    return [
        #Wish("Gain 250 gold", Rarity.COMMON, actions.active_gain_gold(250), [Tag.GOLD]),
        #Wish("Gain 230 gold", Rarity.COMMON, actions.active_gain_gold(230), [Tag.GOLD]),
        #Wish("Gain 220 gold", Rarity.COMMON, actions.active_gain_gold(220), [Tag.GOLD]),

        Wish("Roll a d12. Gain 20x the gold shown", Rarity.COMMON, actions.d12_gold_roll(20), []),
        
        Wish("Gain 320 gold", Rarity.LEGENDARY, actions.active_gain_gold(320), [Tag.GOLD]),
        Wish("The next gold wish doubles the amount of gold you receive", Rarity.LEGENDARY, actions.multiply_next_gold_amount(2, 1), [Tag.GOLD])
    ]
