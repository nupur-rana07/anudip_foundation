import numpy as np

def indices_greater_than(arr, value):
    return np.where(arr > value)[0]   # returns indices

# Example usage
data = np.array([10, 25, 17, 40, 5, 60])
threshold = 20
indices = indices_greater_than(data, threshold)
print("Indices:", indices)