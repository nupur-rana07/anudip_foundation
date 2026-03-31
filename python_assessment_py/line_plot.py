import matplotlib.pyplot as plt

def line_plot(x, y):
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Line Plot")
    plt.grid(True)
    plt.show()

# Example usage
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

line_plot(x, y)