import os
from time import sleep
from play_game import PlayGame
from random import choice


def select_player() -> int:
    player = choice([0, 1])
    return int(player)

def start_game():
    os.system('cls')
    sleep(0.4)
    print("Iniciando o Jogo da Velha...")
    sleep(1.5)
    os.system('cls')
    game = PlayGame()
    game.show_board(sub=True)
    player = game.player
    while not game._win_game() and not game._draw_game():
        if player % 2 == 0:
            print(f"Vez do jogador {player}")
            game._mark_spot_player()
            sleep(0.5)
            player = game.change_player()
        else:
            print(f"Vez do jogador {player}")
            game._mark_spot_cpu()
            sleep(0.5)
            player = game.change_player()
    game.game_over()
    game.define_winner()
    
    
def play_again() -> bool:
        answer = input("Deseja jogar novamente (S/N)? ->  ").upper()
        while answer not in ["S", "N"]:
            answer = input("Deseja jogar novamente (S/N)? ->  ").upper()
        options = {"S": True, "N": False}
        return options[answer]
    
if __name__ == "__main__":
    start_game()
    jogar_novamente = play_again()
    while jogar_novamente:
        start_game()
        jogar_novamente = play_again()
        