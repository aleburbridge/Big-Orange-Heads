def gain_gold(value):
    def gain_value(player):
        player.gold += value

    return gain_value
