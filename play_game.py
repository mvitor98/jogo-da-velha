from fill_game import FillSpots
from game_rules import GameRules


class PlayGame(GameRules):
    
    def __init__(self) -> None:
        super().__init__()
        self.__player:int = 0
    
    def __define_winner(self, player) -> None:
        if player % 2 == 0:
            print("Player 1 win!")
        else:
            print("Player 2 win!")
    
    def play_again(self):
        answer = input("Deseja jogar novamente (S/N)? ->  ").upper()
        while answer not in ["S", "N"]:
            answer = input("Deseja jogar novamente (S/N)? ->  ").upper()
        dict = {"S": True, "N": False}
        return dict[answer]
    
    @property
    def player(self):
        return self.__player
    
            

if __name__ == "__main__":
    game = PlayGame()
    player = game.player
    while game._end_game() is False:
        if player % 2 == 0:
            game._mark_spot_player()
            game._show_matrix()
            player = (player + 1) % 2
            print(f"\nVez do jogador {player}\n")
        else:
            game._mark_spot_cpu()
            game._show_matrix()
            player = (player + 1) % 2
            print(f"\nVez do jogador {player}\n")   
    game._show_matrix()
    game.__define_winner(player)