#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix=[]
    for i in matrix:
        matrx =[]
        for j in range(len(i)):
            matrx.append(i[j] ** 2)
        new_matrix.append(matrx)
    return new_matrix
