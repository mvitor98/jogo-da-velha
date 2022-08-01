from random import choice
from build_game import Matrix

class FillSpots(Matrix):
    
    def __init__(self) -> None:
        super().__init__()
        # self._matrix = [[1, 0, 1] for i in range(3)]
        
    def mark_spot_player(self) -> list:
        row, pos = self.ask_coordinates()
        while not self.verify_play(row=row, pos=pos):
            row, pos = self.ask_coordinates()
        self._matrix[row-1][pos-1] = 1
        self._show_matrix()
        return self._matrix
    
    def mark_spot_cpu(self) -> list:
        row, pos = self.chose_spot()
        while not self.verify_play(row, pos):
            row, pos = self.chose_spot()
        self._matrix[row][pos] = -1
        self._show_matrix()
        return self._matrix
    
    def ask_coordinates(self) -> tuple:
        print("Selecione uma posição no formato (X, Y):")
        row, pos = input("-> ").split(',')
        return int(row), int(pos)
    
    def chose_spot(self) -> tuple:
        row = choice(list(range(len(self._matrix))))
        pos = choice(list(range(self._spots)))
        return row, pos

    def verify_play(self, row:int, pos:int) -> bool:
        try:
            if self._matrix[row][pos] == 0:
                return True
        except:
            return False


if __name__ == "__main__":
    jogo = FillSpots()
    # jogo._show_matrix()
    player = 0
    while True:
        if player % 2 == 0:
            jogo.mark_spot_player()
            player = (player+1)%2
        else:
            jogo.mark_spot_cpu()
            player = (player+1)%2
    # print(jogo.ask_coordinates())