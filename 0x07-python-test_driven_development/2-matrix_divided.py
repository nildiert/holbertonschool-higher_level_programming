#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_list = []
    size_error = "Each row of the matrix must have the same size"
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(type_error)
    if type(div) is not int:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is list:
        for row in matrix:
            if isinstance(row, list):
                len_row = len(matrix[0])
                if len(row) != len_row:
                    raise TypeError(size_error)
                else:
                    for y in row:
                        if type(y) is not int and type(y) is not float:
                            raise TypeError(type_error)
                    new_list.append(list(map(lambda x:
                                             round(x / div, 2), row)))
            else:
                raise TypeError(type_error)
    else:
        raise TypeError(type_error)
    return new_list
