import numpy as np

def normalize(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    return (arr - min_val) / (max_val - min_val)

# Example usage
data = np.array([10, 20, 30, 40, 50])
normalized = normalize(data)
print("Normalized array:", normalized)