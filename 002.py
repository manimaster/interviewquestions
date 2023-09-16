# Manikandan Ramanathan (c) 2019
# For a given array “X,” consisting of non-negative integer characters,
# write a code to find the contiguous subarray with the maximum sum.

def max_subarray_sum(X):
    if not X:
        return []

    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    subarray = []

    for i, num in enumerate(X):
        current_sum += int(num)

        if current_sum > max_sum:
            max_sum = current_sum
            end = i

        if current_sum < 0:
            current_sum = 0
            start = i + 1

    subarray = X[start:end+1]

    return subarray

# Example usage:
X = "235761235"
result = max_subarray_sum(X)
print("Contiguous subarray with maximum sum:", result)
