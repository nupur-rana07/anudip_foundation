import matplotlib.pyplot as plt
import numpy as np

def scatter_with_max(x, y):
    plt.scatter(x, y, color='blue', label='Data Points')

    # Find index of maximum y value
    max_index = np.argmax(y)
    max_x, max_y = x[max_index], y[max_index]

    # Highlight the maximum point
    plt.scatter(max_x, max_y, color='red', s=100, marker='o', label='Maximum Point')
    plt.text(max_x, max_y, f"({max_x}, {max_y})", fontsize=10, ha='left', va='bottom')

    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Scatter Plot with Maximum Point Highlighted")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 8, 22, 17, 19]

scatter_with_max(x, y)