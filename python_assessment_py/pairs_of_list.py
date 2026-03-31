def find_pairs(nums, target):
    pairs = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1, n):  # ensure no duplicate pairs
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    
    return pairs

# Example usage
numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9
print("Pairs with sum =", target, ":", find_pairs(numbers, target))