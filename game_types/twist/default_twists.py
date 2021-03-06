from action import actions
from game_types.twist.Twist import Twist
from game_types.Rarity import Rarity

def default_twists():
    return [
        Twist("Lose 50 gold", Rarity.COMMON, actions.active_sub_gold(50)),
        Twist("Lose 30 gold", Rarity.COMMON, actions.active_sub_gold(30)),
        Twist("Lose 20 gold", Rarity.COMMON, actions.active_sub_gold(20)),

        Twist("Lose 220 gold", Rarity.LEGENDARY, actions.active_sub_gold(220)),
        Twist("Lose 230 gold", Rarity.LEGENDARY, actions.active_sub_gold(230)),
    ]