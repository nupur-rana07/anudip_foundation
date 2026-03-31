def swap_dict(d):
    return {value: key for key, value in d.items()}

# Example usage
data = {"a": 1, "b": 2, "c": 3}
swapped = swap_dict(data)
print("Swapped dictionary:", swapped)