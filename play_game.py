from game_rules import GameRules
from random import choice

class PlayGame(GameRules):
    
    def __init__(self) -> None:
        super().__init__()
        self.player = choice([0, 1])
    
    def game_over(self) -> None:
        self.define_winner()
        print("Fim do jogo!\n")
    
    def define_winner(self) -> int:
        if self._validate_player > 0:
            print("Player X win!\n")
            return 0
        else:
            print("Player O win!\n")
            return 1
    
    def change_player(self) -> int:
        self.player = (self.player + 1) % 2
               

if __name__ == "__main__":
    game = PlayGame()
    while not game._win_game() and not game._draw_game():
        if game.player % 2 == 0:
            game._mark_spot_player()
            game.change_player()
            print(f"\nVez do jogador {game.player}\n")
        else:
            game._mark_spot_cpu()
            game.change_player()
            print(f"\nVez do jogador {game.player}\n")
    game.game_over()
    game.play_again()