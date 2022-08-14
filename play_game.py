from game_rules import GameRules
from random import choice

class PlayGame(GameRules):
    
    def __init__(self) -> None:
        super().__init__()
        self.player = choice([0, 1])
    
    def game_over(self) -> None:
        self.define_winner()
        print("\nFim do jogo!\n")
    
    def define_winner(self) -> int:
        # também posso definir com uma lista. Basta acrescentar o jogador da vez e
        # ver qual foi a última jogada, em caso de vitória.
        if self._validate_player > 0:
            print("Player X win!\n")
            return 0
        else:
            print("Player O win!\n")
            return 1
    
    def change_player(self) -> None:
        self.player = (self.player + 1) % 2
               

if __name__ == "__main__":
    game = PlayGame()
    play_again = True
    while play_again:
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
        opt = input("Deseja jogar novamente (S/N) -> ").lower()
        ans = {"s": True, "n": False}
        play_again = ans[opt]
    # game.play_again()