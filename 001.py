# Manikandan Ramanathan (c) 2019
# For a given unsorted array “X,” consisting of non-negative integers,
# write a code to find the contiguous subarray that adds to the sum “S”
# of non-negative integers in the array.

def find_contiguous_subarray(X, S):
    current_sum = 0
    start = 0
    subarray = []

    for end, num in enumerate(X):
        current_sum += num

        while current_sum > S:
            current_sum -= X[start]
            start += 1

        if current_sum == S:
            subarray = X[start:end+1]
            break

    return subarray

# Example usage:
X = [1, 2, 3, 4, 5]
S = 9
result = find_contiguous_subarray(X, S)
print("Contiguous subarray that adds up to", S, ":", result)
