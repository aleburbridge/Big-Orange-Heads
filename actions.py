def active_gain_gold(value):
    def gain_value(game):
        game.active_player().gold += value

    return gain_value

def d12_gold_roll_function(multiplier):
    def perform_d12_roll(game):
        roll_result = game.active_player().dice.perform_d12_roll(game)
        game.active_player().gold += roll_result * multiplier
    return perform_d12_roll
