import matplotlib.pyplot as plt

def pie_chart(categories, values):
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90,
            colors=['skyblue', 'lightgreen', 'orange', 'pink', 'purple'])
    plt.title("Percentage Distribution")
    plt.axis('equal')  # ensures the pie is a circle
    plt.show()

# Example usage
categories = ["Category A", "Category B", "Category C", "Category D"]
values = [25, 35, 20, 20]

pie_chart(categories, values)