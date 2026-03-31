import numpy as np

def matrix_multiply(A, B):
    return np.matmul(A, B)   # or A @ B

# Example usage
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = matrix_multiply(A, B)
print("Result matrix:\n", result)