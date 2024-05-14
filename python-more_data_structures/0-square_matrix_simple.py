#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for index_row in range(len(matrix)):
        row = []
        for index_column in range(len(matrix[index_row])):
            row.append(matrix[index_row][index_column] ** 2)
        new_matrix.append(row)
    return new_matrix
