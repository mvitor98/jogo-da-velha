from game_rules import GameRules


class PlayGame(GameRules):
    
    def __init__(self) -> None:
        super().__init__()
        self.player = 0
    
    def game_over(self) -> bool:
        print("Fim do jogo!\n")
    
    def define_winner(self) -> None:
        if self._validate_player > 0:
            print("Player X win!\n")
        else:
            print("Player O win!\n")
    
    def change_player(self) -> int:
        self.player = (self.player + 1) % 2
        return self.player

               

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