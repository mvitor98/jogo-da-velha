from fill_game import FillSpots
from game_rules import GameRules


class PlayGame():
    
    def __init__(self) -> None:
        self.__rules = GameRules()
        self._plays = FillSpots()

    def play_game(self):
        



