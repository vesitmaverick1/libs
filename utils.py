def karatsuba(num1: int, num2: int) -> int:
    """
    Multiplies two large numbers using the Karatsuba algorithm.
    Time Complexity: O(N^1.58)
    Example Usage (Python natively casts strings to large ints for this math):
    val1 = 123456789123456789
    val2 = 987654321987654321
    print(karatsuba(val1, val2))
    """
    # Base case for small numbers
    if num1 < 10 or num2 < 10:
        return num1 * num2
        
    # Calculate the size of the numbers
    n = max(len(str(num1)), len(str(num2)))
    half = n // 2
    
    # Split the digit sequences in the middle
    # Example: 1234 -> a = 12, b = 34
    a = num1 // (10 ** half)
    b = num1 % (10 ** half)
    c = num2 // (10 ** half)
    d = num2 % (10 ** half)
    
    # Recursively calculate the 3 required products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    
    # Recompose the final result using the Karatsuba formula
    return (ac * (10 ** (2 * half))) + (ad_plus_bc * (10 ** half)) + bd

def sum_large_strings(num1: str, num2: str) -> str:
    """
    Sums two incredibly large integers represented as strings.
    Time Complexity: O(N) where N is the length of the longer string.
    Example Usage:
    n1 = "99999999999999999999"
    n2 = "1"
    print(sum_large_strings(n1, n2)) 
    Output: "100000000000000000000"
    """
    result = []
    carry = 0
    
    # Pointers starting at the end (least significant digit) of each string
    i = len(num1) - 1
    j = len(num2) - 1
    
    # Loop as long as there are digits to process or a carry left over
    while i >= 0 or j >= 0 or carry:
        # Get the current digit value, or 0 if we've run out of digits
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        
        # Calculate total and determine the new carry
        current_sum = digit1 + digit2 + carry
        carry = current_sum // 10
        remainder = current_sum % 10
        
        # Append the current single digit to our result list
        result.append(str(remainder))
        
        # Move pointers to the left
        i -= 1
        j -= 1
        
    # Since we added digits from right to left, reverse the result list
    return "".join(reversed(result))

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
