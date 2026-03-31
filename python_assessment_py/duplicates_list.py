def remove_duplicates(lst):
    result = []
    seen = {}
    for item in lst:
        if item not in seen:
            result.append(item)
            seen[item] = True
    return result

# Example usage
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
print("List without duplicates:", remove_duplicates(numbers))