#!/usr/bin/python3
"""
    The module ``2-matrix_divided``

    This module contains one function ``matrix_divided()``
"""


def matrix_divided(matrix, div):
    """
        divides a matrix
    """
    result_matrix = []
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        + " of integers/floats")
    if not type(div) in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    column_count = None
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of"
                            + " lists) of integers/floats")
        new_row = []
        i = 0
        for element in row:
            if not type(element) in [int, float]:
                raise TypeError("matrix must be a matrix (list"
                                + " of lists) of integers/floats")
            calculation = element / div
            two_decimal_place = float("{:.2f}".format(calculation))
            new_row.append(two_decimal_place)
            i += 1
        if column_count is None:
            column_count = i
        else:
            if column_count != i:
                raise TypeError("Each row of the matrix"
                                +"  must have the same size")
        result_matrix.append(new_row)

    return result_matrix
