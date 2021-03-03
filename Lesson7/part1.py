from random import randrange


class Matrix():

    def __init__(self, matrix_1, matrix_2, new_matrix):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
        self.new_matrix = new_matrix

    def __add__(self):
        for i in range(len(self.matrix_1)):
            for j in range(len(self.matrix_2)):
                self.new_matrix[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]
        return self.new_matrix

    def __str__(self):
        print(str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix])))


n = randrange(2, 5)
matrix_1 = [[randrange(1, 5) for j in range(n)] for i in range(n)]
matrix_2 = [[randrange(1, 5) for j in range(n)] for i in range(n)]
new_matrix = [[0 for j in range(n)] for i in range(n)]
print(f'Сгенерированная матрица 1 - {matrix_1}')
print(f'Сгенерированная матрица 2 - {matrix_2}')
m = Matrix(matrix_1, matrix_2, new_matrix)
print(f'Сложение матриц - {m.__add__()}')
print("Итоговая матрица в привычном виде -")
m.__str__()
