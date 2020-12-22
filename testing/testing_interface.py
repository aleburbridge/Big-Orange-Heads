from Choice import Choice
from player import Player


class TestingInterface:
    def player_choose(self, player: Player, choices: list[Choice]):
        return choices[0]