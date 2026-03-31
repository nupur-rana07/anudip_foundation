def is_armstrong(n):
    # Convert number to string to count digits
    digits = str(n)
    power = len(digits)
    
    total = 0
    for d in digits:
        total += int(d) ** power
    
    return total == n

# Example usage
num = 153
print("Is Armstrong:", is_armstrong(num))  # True