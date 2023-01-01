"""
Write a Python program to compute following computation on matrix:
a) Addition of two matrices 
b) Multiplication of two matrices
c) Transpose of a matrix
"""



def matrix_addition(A, B):
    # Check if the matrices are the same size
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: Matrices are not the same size"

    # Create a new matrix to store the result
    C = []

    # Perform element-wise addition of the matrices
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[0])):
            C[i].append(A[i][j] + B[i][j])

    return C

def matrix_multiplication(A, B):
    # Check if the matrices can be multiplied (A's columns must be the same size as B's rows)
    if len(A[0]) != len(B):
        return "Error: Matrices cannot be multiplied"

    # Create a new matrix to store the result
    C = []

    # Perform matrix multiplication
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            total = 0
            for k in range(len(A[0])):
                total += A[i][k] * B[k][j]
            C[i].append(total)

    return C

def matrix_transpose(A):
    # Create a new matrix to store the transpose
    transpose = []

    # Transpose the matrix
    for i in range(len(A[0])):
        transpose.append([])
        for j in range(len(A)):
            transpose[i].append(A[j][i])

    return transpose

# Test the functions
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = matrix_addition(A, B)
print("Matrix addition:")
print(C)

C = matrix_multiplication(A, B)
print("Matrix multiplication:")
print(C)

C = matrix_transpose(A)
print("Matrix transpose:")
print(C)
