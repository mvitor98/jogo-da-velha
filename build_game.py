
class Matrix:
    
    def __init__(self) -> None:
        self._spots = 3
        self._matrix = self.__build_matrix()
    
    def __build_matrix_line(self) -> list:
        return list(0 for i in range(self._spots))
    
    def __build_matrix(self) -> list:
        return list(self.__build_matrix_line() for i in range(self._spots))
    
    def _show_matrix(self) -> None:
        print('   1  2  3')
        for index, row in enumerate(self._matrix, 1):
            print(index, row)

if __name__ == "__main__":
    jogo = Matrix()
    jogo._show_matrix()
    # print(len(jogo._matrix))
    