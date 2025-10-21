import numpy as np
from sympy import Matrix
from functools import reduce

def sum(matrices):
    return np.sum(matrices, axis=0)

def subtract(matrices):
    return reduce(np.subtract, matrices)

def multiply(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

def divide(matrix_a, matrix_b):
    return np.divide(matrix_b, matrix_a)

def inverse(matrix):
    return np.linalg.inv(matrix)

def transpose(matrix):
    return np.transpose(matrix)

def rank(matrix):
    return np.linalg.matrix_rank(matrix)

def determinant(matrix):
    return np.linalg.det(matrix)

def eigenvalues(matrix):    
    return np.linalg.eigvals(matrix)

def eigenvectors(matrix):
    return np.linalg.eig(matrix)[1]

def upper_triangular(matrix):
    return np.triu(matrix)

def lower_triangular(matrix):
    return np.tril(matrix)

def scaled_echelon_form(matrix):
    return np.array(Matrix(matrix).echelon_form()).astype(float)