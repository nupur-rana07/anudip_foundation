import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, bins=10):
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black')
    plt.xlabel("Value Range")
    plt.ylabel("Frequency")
    plt.title("Histogram of Dataset")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Example usage
# Generate a random dataset
data = np.random.randint(1, 100, size=50)

plot_histogram(data, bins=8)