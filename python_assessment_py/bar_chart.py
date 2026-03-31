import matplotlib.pyplot as plt

def bar_chart(products, sales):
    plt.bar(products, sales, color=['blue', 'green', 'red', 'orange', 'purple'])
    plt.xlabel("Products")
    plt.ylabel("Sales")
    plt.title("Product Sales Bar Chart")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Example usage
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = [120, 90, 150, 80, 200]

bar_chart(products, sales)