from numpy import transpose
from fill_game import FillSpots

class GameRules(FillSpots):
    
    def __init__(self) -> None:
        super().__init__()
        self.__matrix = self._matrix
        self._validate_player = 0
        # self._matrix_col = [[0, 0, -1], [0, 0, -1], [0, 0, -1]]
        # self._matrix_line = [[-1, -1, -1], [0, 0, -1], [0, 0, -1]]
        # self._matrix_diag_asc = [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]
        # self._matrix_diag_desc = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        # self._matrix = [[-1, -1, 1], [-1, 1, -1], [-1, -1, 1]]
        
    def __define_winner(self, result:int) -> None:
        if result > 0:
            self._validate_player= 1
        else:
            self._validate_player = -1    
        
    def _win_game_by_line(self) -> bool:
        # self._matrix = self._matrix_line
        for index, row in enumerate(self.__matrix):
            sum_row = sum(row)
            if sum_row in [-3, 3]:
                print(f"Won by line {index + 1}!")
                self.__define_winner(sum_row)
                return True
        return False
    
    def _win_game_by_col(self) -> bool:
        # self._matrix = self._matrix_col
        transpose_matrix = transpose(self.__matrix).tolist()
        for index, row in enumerate(transpose_matrix):
            sum_col = sum(row)
            if sum_col in [-3, 3]:
                print(f"Won by column {index + 1}!")
                self.__define_winner(sum_col)
                return True
        return False
        
    def _win_game_by_diagonal_desc(self) -> bool:
        # self._matrix = self._matrix_diag_desc
        sum_diagonal = sum(self.__matrix[i][i] for i in range(len(self.__matrix)))
        if sum_diagonal in [-3, 3]:
            print("Won by descendent diagonal!")
            self.__define_winner(sum_diagonal)
            return True
        return False
    
    def _win_game_by_diagonal_asc(self) -> bool:
        # self._matrix = self._matrix_diag_asc
        self.__matrix.reverse()
        sum_reverse_diagonal = sum(self.__matrix[i][i] for i in range(len(self.__matrix)))
        if sum_reverse_diagonal in [-3, 3]:
            print("Won by ascendent diagonal")
            self.__define_winner(sum_reverse_diagonal)
            return True
        return False
    
    def _win_game(self) -> bool:
        if (self._win_game_by_line()|
            self._win_game_by_col()|
            self._win_game_by_diagonal_asc()|
            self._win_game_by_diagonal_asc()):
            return True
        else:
            return False
    
    def _draw_game(self) -> bool:
        if not self._win_game() and self.count_empty_spots() > 0:
            return False
        else:
            print("Draw! Try again...")
            return True     
            
    
if __name__ == '__main__':
    jogo = GameRules()
    player = 0
    play_game = True
    while play_game:
        if player % 2 == 0:
            jogo._mark_spot_player()
            jogo._show_matrix()
            player = (player+1)%2
        else:
            jogo._mark_spot_cpu()
            player = (player+1)%2