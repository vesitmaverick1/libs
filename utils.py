def find_two_sum(nums: list, target: int) -> list:
    """
    Finds the indices of the two numbers that add up to the target.
    Time Complexity: O(n) - Loops through the list once.
    Space Complexity: O(n) - Stores elements in a dictionary.
    """
    seen = {}  # Dictionary to store: { number: its_index }
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # If the complement is already in our dictionary, we found the pair!
        if complement in seen:
            return [seen[complement], index]
        
        # Otherwise, add the current number and its index to the dictionary
        seen[num] = index
        
    return []  # Return empty list if no pair is found

# Example Usage:
numbers_list = [2, 7, 11, 15]
target_sum = 9

result = find_two_sum(numbers_list, target_sum)
print(f"Indices of numbers that add up to {target_sum}: {result}")
# Output: [0, 1] (because numbers_list[0] + numbers_list[1] -> 2 + 7 = 9)
