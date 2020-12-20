def active_gain_gold(value):
    def gain_value(game):
        game.active_player().gold += value

    return gain_value
