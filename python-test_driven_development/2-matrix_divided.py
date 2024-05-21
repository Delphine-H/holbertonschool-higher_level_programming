#!/usr/bin/python3
"""
This module contain a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
    matrix (list of lists of int/float): A matrix to be divided.
        Each sublist represents a row.
    div (int/float): The divisor by which each element of the
    matrix will be divided.

    Returns:
    list of lists of float: A new matrix with each element divided
    by the divisor, rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats,
    if rows of the matrix are not of the same size,
    or if div is not a number (integer or float).
    ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list)) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
            new_row.append(round(element / div, 2))
        result.append(new_row)
    return result
