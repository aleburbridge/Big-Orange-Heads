from action_stack import ActionStack
from action import Action, UseAction

def active_gain_gold(value):
    def gain_value(game):
        player = game.active_player()
        player.add_gold_instant(value)

    return gain_value

def d12_gold_roll(multiplier):
    def perform_d12_roll(game):
        player = game.active_player()
        roll_result = game.active_player().dice.perform_d12_roll(game)
        player.add_gold_instant(roll_result * multiplier)
    return perform_d12_roll

def multiply_next_gold_amount(amount, num_uses):
    def apply_modifier(game):
        def multiplier(gold):
            if gold_multiplier_action.num_uses > 0:
                gold_multiplier_action.num_uses -= 1
                return gold * amount 
            return gold

        gold_multiplier_action = UseAction(multiplier, 1, [], num_uses)
        for victim in game.victims:
            victim.gold_modifiers.append(gold_multiplier_action)
    return apply_modifier
