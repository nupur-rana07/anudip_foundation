def first_non_repeating(s):
    freq = {}
    
    # Count frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find the first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char
    
    return None  # If no non-repeating character exists

# Example usage
text = "swiss"
print("First non-repeating character:", first_non_repeating(text))