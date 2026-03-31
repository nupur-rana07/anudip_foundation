import numpy as np

def stats(arr):
    mean_val = np.mean(arr)
    median_val = np.median(arr)
    std_val = np.std(arr)
    return mean_val, median_val, std_val

# Example usage
data = np.array([10, 20, 30, 40, 50])
mean, median, std = stats(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)