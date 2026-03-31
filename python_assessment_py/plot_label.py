import matplotlib.pyplot as plt

def styled_plot(months, revenue):
    plt.plot(months, revenue, marker='o', linestyle='-', color='green')

    # Add labels and title
    plt.xlabel("Months")
    plt.ylabel("Revenue (in $)")
    plt.title("Monthly Revenue Trend")

    # Add grid for readability
    plt.grid(True, linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()

# Example usage
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1200, 1500, 1100, 1800, 1700, 2000]

styled_plot(months, revenue)