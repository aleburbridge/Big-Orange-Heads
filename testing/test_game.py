from unittest import TestCase

from game import Game
from testing.testing_interface import TestingInterface


class TestGame(TestCase):
    def test_start_game(self):
        self.game = Game("tester1 tester2 tester3 tester4", TestingInterface())
