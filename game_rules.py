from numpy import transpose
from fill_game import FillSpots

class GameRules(FillSpots):
    
    def __init__(self) -> None:
        super().__init__()
        self.__matrix = self._matrix
        # self._matrix_col = [[0, 0, -1], [0, 0, -1], [0, 0, -1]]
        # self._matrix_line = [[-1, -1, -1], [0, 0, -1], [0, 0, -1]]
        # self._matrix_diag_asc = [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]
        # self._matrix_diag_desc = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        # self._matrix = [[-1, -1, 1], [-1, 1, -1], [-1, -1, 1]]
        
    def _win_game_by_line(self) -> bool:
        # self._matrix = self._matrix_line
        for index, row in enumerate(self.__matrix):
            sum_row = sum(row)
            if sum_row == 3 or sum_row == -3:
                print(f"Won by line {index}")
                self._show_matrix()
                return True
        return False
    
    def _win_game_by_col(self) -> bool:
        # self._matrix = self._matrix_col
        transpose_matrix = transpose(self.__matrix).tolist()
        for index, row in enumerate(transpose_matrix):
            sum_col = sum(row)
            if sum_col == 3 or sum_col == -3:
                print(f"Won by column {index+1}")
                self._show_matrix()
                return True
        return False
        
    def _win_game_by_diagonal_asc(self) -> bool:
        # self._matrix = self._matrix_diag_desc
        diagonal_sum = sum(self.__matrix[i][i] for i in range(len(self.__matrix)))
        if diagonal_sum == 3 or diagonal_sum == -3:
            self._show_matrix()
            return True
        return False
    
    def _win_game_by_diagonal_desc(self) -> bool:
        # self._matrix = self._matrix_diag_asc
        self.__matrix.reverse()
        reverse_diagonal_sum = sum(self.__matrix[i][i] for i in range(len(self.__matrix)))
        if reverse_diagonal_sum == 3 or reverse_diagonal_sum == -3:
            self._show_matrix()
            return True
        return False
    
    def _win_game(self) -> bool:
        while not(self._win_game_by_line()|self._win_game_by_col()|self._win_game_by_diagonal_asc()|self._win_game_by_diagonal_asc()):
            return False
        return True
    
    def _draw_game(self) -> bool:
        if not self._win_game():
            return True
        else:
            return False
        
    def _end_game(self) -> bool:
        while not self._win_game() or not self._draw_game():
            return False
        return True
        
    
if __name__ == '__main__':
    # rules._show_matrix()
    # print(rules.transpose_matrix())
    # print(f"Column win: {rules.win_game_by_col()}")
    # print(f"Diagonal ASC: {rules.win_game_by_diagonal_asc()}")
    # print(f"Diagonal DESC: {rules.win_game_by_diagonal_desc()}")
    pass
    