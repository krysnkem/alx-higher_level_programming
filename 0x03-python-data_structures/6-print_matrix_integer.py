#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return;
    matrix_len = len(matrix)
    last_row_idx = matrix_len - 1
    for row_index in range(matrix_len):
        row_length = len(matrix[row_index])
        last_elem_idx = row_length - 1
        for idx in range(row_length):
            print("{:d}".format(matrix[row_index][idx]), end="")
            if idx < last_elem_idx:
                print("", end=" ")

        if row_index < last_row_idx:
            print()

    print()
