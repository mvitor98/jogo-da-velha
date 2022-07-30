from numpy import transpose

matrix = [[1,0,0], [0,1,0], [0,0,1]]

for row in matrix: print(row)
print(40*"-")

transposed_matrix = transpose(matrix).tolist()
transposed_matrix2 = transpose(transposed_matrix).tolist()
# for row in transposed_matrix: print(row)
# print(40*"-")
# for row in transposed_matrix2: print(row)
# print(type(transpose_matrix))
# print(type(transpose_matrix()))

# for a, b in enumerate(matrix):
#     print(a, " - ",b)

matrix_r =matrix.reverse()
for row in matrix_r : print(row)