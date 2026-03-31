def sort_by_marks(data):
    # Sort by the second element (marks) in each tuple
    return sorted(data, key=lambda x: x[1])

# Example usage
students = [("Alice", 88), ("Bob", 75), ("Charlie", 95), ("David", 82)]
sorted_students = sort_by_marks(students)
print("Sorted list:", sorted_students)