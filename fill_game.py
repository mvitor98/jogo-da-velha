from random import choice
from build_game import Matrix

class FillSpots(Matrix):
      
    def __init__(self) -> None:
        super().__init__()
    
    def count_empty_spots(self):
        zeros = 0
        for row in self._matrix:
            for pos in row:
                if pos == 0:
                    zeros += 1
        return zeros
        
    def _mark_spot_player(self) -> None:
        row, pos = self.__verify_player_play()
        self._matrix[row][pos] = 1
        print(f"Posições escolidas: ({row}, {pos})")
        self.show_board(sub=True)
            
    def _mark_spot_cpu(self) -> None:
        row, pos = self.__verify_cpu_play()
        self._matrix[row][pos] = -1
        print(f"Posições escolidas: ({row}, {pos})")
        self.show_board(sub=True)
        
    def __ask_coordinates(self) -> tuple:
        print("Selecione uma posição no formato (linha, posição):")
        try:
            row, pos = input("-> ").split(',')
            while int(row) < 1 or int(row) > 3 or int(row) < 1 or int(pos) > 3:
                print(f"Posições inválidas. Digite APENAS números entre 1 e 3.")
                row, pos = self.__ask_coordinates()
                print(f"Posições escolidas: ({row}, {pos})")
        except ValueError:
            print("Valor informado inválido. Digite APENAS números entre 1 e 3.")
            print(f"Posições inválidas. Digite APENAS números entre 1 e 3.")
            row, pos = self.__ask_coordinates()
            print(f"Posições escolidas: ({row}, {pos})")
            row += 1
            pos += 1
        return int(row)-1, int(pos)-1
    
    def __chose_spot(self) -> tuple:
        row = choice(list(range(len(self._matrix))))
        pos = choice(list(range(self._spots)))
        return (row, pos)

    def __verify_player_play(self) -> tuple:
        row, pos = self.__ask_coordinates()
        while self._matrix[row][pos] in [1, -1]:
            print(f"Ponto ({row+1},{pos+1}) ja á está preenchido!")
            row, pos = self.__ask_coordinates()
        return (int(row), int(pos))
    
    def __verify_cpu_play(self):
        row, pos = self.__chose_spot()
        while self._matrix[row][pos] != 0:
            row, pos = self.__chose_spot()
        return row, pos

if __name__ == "__main__":
    jogo = FillSpots()
    # jogo._show_matrix()
    player = 0
    # while True:
    #     if player % 2 == 0:
    #         jogo._mark_spot_player()
    #         player = (player+1)%2
    #     else:
    #         jogo._mark_spot_cpu()
    #         player = (player+1)%2
    jogo._mark_spot_player()
    jogo.show_board()
    # print(jogo.ask_coordinates())