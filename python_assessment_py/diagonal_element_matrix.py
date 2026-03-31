import numpy as np

def extract_diagonal(matrix):
    return np.diagonal(matrix)

# Example usage
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

diagonal_elements = extract_diagonal(arr)
print("Diagonal elements:", diagonal_elements)