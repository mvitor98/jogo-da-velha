from random import choice

from numpy import choose
from build_game import Matrix

class FillSpots(Matrix):
    
    def __init__(self) -> None:
        super().__init__()
        # self._matrix = [[1, 0, 1] for i in range(3)]
        
    def _mark_spot_player(self) -> list:
        row, pos = self.__verify_player_play()
        self._matrix[row-1][pos-1] = 1
        return self._matrix
    
    def _mark_spot_cpu(self) -> list:
        row, pos = self.__verify_cpu_play()
        self._matrix[row][pos] = -1
        return self._matrix
    
    def __ask_coordinates(self) -> tuple:
        print("Selecione uma posição no formato (linha, posição):")
        try:
            row, pos = input("-> ").split(',')
            while int(row) < 1 or int(row) > 3 or int(row) < 1 or int(pos) > 3:
                print(f"Posições inválidas. Digite APENAS números entre 1 e 3.")
                row, pos = self.__ask_coordinates()
            return int(row), int(pos)
        except ValueError:
            print("Valor informado inválido. Digite APENAS números entre 1 e 3.")
            row, pos = self.__ask_coordinates()
    
    def __chose_spot(self) -> tuple:
        row = choice(list(range(len(self._matrix))))
        pos = choice(list(range(self._spots)))
        return row, pos

    def __verify_player_play(self) -> bool:
        row, pos = self.__ask_coordinates()
        while self._matrix[row][pos] == 1 or self._matrix[row][pos] == -1:
            print(f"Ponto ({row},{pos}) ja á está preenchido!")
            row, pos = self.__ask_coordinates()
        return row, pos
    
    def __verify_cpu_play(self):
        row, pos = self.__chose_spot()
        while self._matrix[row][pos] in [-1, 1]:
            row, pos = self.__chose_spot()
        return row, pos

if __name__ == "__main__":
    jogo = FillSpots()
    # jogo._show_matrix()
    player = 0
    while True:
        if player % 2 == 0:
            jogo._mark_spot_player()
            jogo._show_matrix()
            # player = (player+1)%2
        else:
            jogo._mark_spot_cpu()
            player = (player+1)%2
    # print(jogo.ask_coordinates())