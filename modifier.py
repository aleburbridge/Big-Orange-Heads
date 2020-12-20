class Modifier:
    def __init__(self, turn, value, turns_before_expiration):
        self.turn = turn
        self.value = value
        self.turns_before_expiration = turns_before_expiration

    def is_expired(self, cur_turn):
        # e.g.: called on turn 9, created on turn 8, 1 turn before expiration
        # 9-8 > 1 = false (still use it; delete on the next turn)
        return (cur_turn - self.turn > self.turns_before_expiration)