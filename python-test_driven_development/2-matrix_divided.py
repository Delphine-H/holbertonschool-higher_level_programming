#!/usr/bin/python3


def matrix_divided(matrix, div):
	"""
    Divides all elements of a matrix by a given divisor.
    
    Parameters:
    matrix (list of lists of int/float): A matrix to be divided. Each sublist represents a row.
    div (int/float): The divisor by which each element of the matrix will be divided.
    
    Returns:
    list of lists of float: A new matrix with each element divided by the divisor, rounded to 2 decimal places.
    
    Raises:
    TypeError: If matrix is not a list of lists of integers/floats, if rows of the matrix are not of the same size,
               or if div is not a number (integer or float).
    ZeroDivisionError: If div is zero.
    """
	if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
		raise TypeError("matrix must be a matrix (list or lists) of integers/floats")
	if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
		raise TypeError("Each row of the matrix must have the same size")
	if not isinstance(div, int) or not isinstance(div, float):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")
	result = []
	for row in matrix:
		new_row = []
		for elements in row:
			if not isinstance(elements, (int, float)):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
		new_row.append(round(elements / div, 2))
	result.append(new_row)
	return result
