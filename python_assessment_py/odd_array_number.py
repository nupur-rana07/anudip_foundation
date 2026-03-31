import numpy as np

def replace_odds(arr):
    arr[arr % 2 != 0] = -1
    return arr

# Example usage
data = np.array([1, 2, 3, 4, 5, 6, 7])
modified = replace_odds(data)
print("Modified array:", modified)