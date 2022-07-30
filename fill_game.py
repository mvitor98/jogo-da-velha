from random import choice, randint
from build_game import Matrix

class FillSpots(Matrix):
    
    def __init__(self) -> None:
        super().__init__()
        # self._matrix = [[1, 0, 1] for i in range(3)]
        
    def mark_spot(self, player) -> list:
        row, pos = self.chose_spot()
        if player % 2 == 0:
            self._matrix[row][pos] = 1
        else:
            self._matrix[row][pos] = -1
        self._show_matrix()
        return self._matrix
    
    def chose_spot(self) -> int:
        row = choice(list(range(len(self._matrix))))
        pos = choice(list(range(self._spots)))
        while not self.verify_play(row=row, pos=pos):
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
    jogo.mark_spot(1)