import os
from time import sleep
from play_game import PlayGame

class StartGame(PlayGame):
    def __init__(self) -> None:
        super().__init__()
            
    def start_game(self) -> None:
        os.system('cls')
        sleep(0.4)
        print("Iniciando o Jogo...")
        sleep(1.5)
        os.system('cls')
        self.show_board(sub=True)
        while not self._win_game() and not self._draw_game():
            if self.player % 2 == 0:
                print(f"Vez do jogador X")
                self._mark_spot_player()
                sleep(0.5)
                self.change_player()
            else:
                print(f"Vez do jogador O")
                self._mark_spot_cpu()
                sleep(0.5)
                self.change_player()
        self.game_over()
        
    def play_again(self) -> bool:
        answer = input("Deseja jogar novamente (S/N)? ->  ").upper()
        while answer not in ["S", "N"]:
            answer = input("Deseja jogar novamente (S/N)? ->  ").upper()
        options = {"S": True, "N": False}
        return options[answer]

if __name__ == "__main__":
    game = StartGame()
    game.start_game()
    jogar_novamente = game.play_again()
    while jogar_novamente:
        game = StartGame()
        game.start_game()
        jogar_novamente = game.play_again()
        