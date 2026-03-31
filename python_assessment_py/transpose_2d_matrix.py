import numpy as np

def transpose_matrix(matrix):
    return matrix.T   # or np.transpose(matrix)

# Example usage
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

transposed = transpose_matrix(arr)
print("Original matrix:\n", arr)
print("Transposed matrix:\n",transposed)