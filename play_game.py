from fill_game import FillSpots
from game_rules import GameRules


class PlayGame():
    
    def __init__(self) -> None:
        self.__rules = GameRules()
        self._plays = FillSpots()

    def _play_game(self) -> None:
        while not self._end_game():
            game = self._plays()

    def _end_game(self):
        while not(self.__rules._win_game() or self.__rules._draw_game()):
            return False

