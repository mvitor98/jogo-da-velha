from fill_game import FillSpots
from numpy import transpose

class GameRules(FillSpots):
    
    def __init__(self) -> None:
        super().__init__()
        # self._matrix_col = [[0, 0, -1], [0, 0, -1], [0, 0, -1]]
        # self._matrix_line = [[-1, -1, -1], [0, 0, -1], [0, 0, -1]]
        # self._matrix_diag_asc = [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]
        # self._matrix_diag_desc = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        
    def _win_game_by_line(self):
        # self._matrix = self._matrix_line
        for row in self._matrix:
            sum_row = sum(row)
            if sum_row == 3 or sum_row == -3:
                self.define_winner()
                return True
        return False
    
    def _win_game_by_col(self):
        # self._matrix = self._matrix_col
        transpose_matrix = transpose(self._matrix).tolist()
        print(transpose_matrix)
        for index, row in enumerate(transpose_matrix):
            sum_col = sum(row)
            if sum_col == 3 or sum_col == -3:
                self.define_winner(sum_col)
                print(f"Won by column {index+1}")
                return True
        return False
        
    def _win_game_by_diagonal_asc(self):
        # self._matrix = self._matrix_diag_desc
        diagonal_sum = sum(self._matrix[i][i] for i in range(len(self._matrix)))
        if diagonal_sum == 3 or diagonal_sum == -3:
            self._define_winner()
            return True
        return False
    
    def _win_game_by_diagonal_desc(self):
        # self._matrix = self._matrix_diag_asc
        self._matrix.reverse()
        reverse_diagonal_sum = sum(self._matrix[i][i] for i in range(len(self._matrix)))
        if reverse_diagonal_sum == 3 or reverse_diagonal_sum == -3:
            self._define_winner()
            return True
        return False
        
    def _define_winner(self, sum:int) -> None:
        if sum > 0:
            print("Player 2 win!")
        else:
            print("Player 1 win!")
        
if __name__ == '__main__':
    rules = GameRules()
    # rules._show_matrix()
    # print(rules.transpose_matrix())
    # print(f"Column win: {rules.win_game_by_col()}")
    # print(f"Diagonal ASC: {rules.win_game_by_diagonal_asc()}")
    print(f"Diagonal DESC: {rules.win_game_by_diagonal_desc()}")
    