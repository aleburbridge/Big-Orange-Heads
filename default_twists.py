import actions
from Twist import Twist
from rarity import Rarity

def default_twists():
    return [
        Twist("Lose 50 gold", Rarity.COMMON, actions.gain_gold(-50)),
        Twist("Lose 30 gold", Rarity.COMMON, actions.gain_gold(-30)),
        Twist("Lose 20 gold", Rarity.COMMON, actions.gain_gold(-20)),

        Twist("Lose 220 gold", Rarity.LEGENDARY, actions.gain_gold(-220)),
        Twist("Lose 230 gold", Rarity.LEGENDARY, actions.gain_gold(-230)),
    ]