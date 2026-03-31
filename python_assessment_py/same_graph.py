import matplotlib.pyplot as plt

def plot_two_datasets(x1, y1, x2, y2, label1="Dataset 1", label2="Dataset 2"):
    plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label=label1)
    plt.plot(x2, y2, marker='s', linestyle='--', color='red', label=label2)
    
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Combined Plot of Two Datasets")
    plt.legend()  # adds legend
    plt.grid(True)
    plt.show()

# Example usage
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

plot_two_datasets(x1, y1, x2, y2, "Linear Growth", "Slightly Slower Growth")