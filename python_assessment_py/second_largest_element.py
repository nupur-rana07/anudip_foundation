def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements
    
    largest = second = float('-inf')
    
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else None

# Example usage
numbers = [12, 35, 1, 10, 34, 1]
print("Second largest element:", second_largest(numbers))