import numpy as np

def elementwise_multiply(arr1, arr2):
    return arr1 * arr2   # or np.multiply(arr1, arr2)

# Example usage
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

result = elementwise_multiply(a, b)
print("Resultant array:", result)