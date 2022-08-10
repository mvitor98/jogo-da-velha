import os
from time import sleep

class Matrix:
    
    def __init__(self) -> None:
        self._spots = 3
        self._matrix = self.__build_matrix()
    
    def __build_matrix_line(self) -> list:
        return list(0 for i in range(self._spots))
    
    def __build_matrix(self) -> list:
        return list(self.__build_matrix_line() for i in range(self._spots))

    def show_board(self, sub:bool=False) -> None:
        os.system('cls')
        blank_space = " "*3
        print(blank_space+'     1     2     3\n')
        if sub:
            sub_item = {
                 0: '   ',
                 1: ' X ',
                -1: ' O '
            }
            for index, row in enumerate(self._matrix, 1):
                print(index, blank_space," |".join(" "*( 4 - len( str( sub_item[i] ) ) ) + str(sub_item[i]) for i in row), "\n")
        else:
            for index, row in enumerate(self._matrix, 1):
                print(index, blank_space,"  |".join(" "*(3-len(str(i)))+str(i) for i in row), "\n")

if __name__ == "__main__":
    jogo = Matrix()
    jogo.show_board()
    # print(len(jogo._matrix))
    