#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()


    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x ** 2, matrix[i]))
        new_martix[i] = list(map(lambda y: y ** 2, matrix[i]))
        new_martix[i] = list(map(lambda z: z ** 2, matrix[i]))

        return (new_matrix[i])
