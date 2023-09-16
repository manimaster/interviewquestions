# Manikandan Ramanathan (c) 2019
# For a given array “X” of size N-1 consisting of numbers from 1 to N
# with one number missing, write a code to find the missing number in the array.

def find_missing_number(X, N):
    total_sum = (N * (N + 1)) // 2  # Sum of all numbers from 1 to N
    array_sum = sum(X)
    missing_number = total_sum - array_sum
    return missing_number

# Example usage:
X = [1, 2, 4, 5, 6]
N = 6
result = find_missing_number(X, N)
print("Missing number in the array:", result)
