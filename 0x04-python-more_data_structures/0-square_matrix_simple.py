#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_square = list(list(map(lambda x: x ** 2, per_row)) for per_row in matrix)
    return matrix_square

