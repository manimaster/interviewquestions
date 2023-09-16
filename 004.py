# Manikandan Ramanathan (c) 2019
# For a given set of 2 sorted arrays “X” and “Y” with respective sizes “n” and ‘m’,
# write a code to merge the two sorted arrays such that their characters appear in decreasing order.

def merge_sorted_arrays_decreasing(X, Y):
    merged_array = []
    i = len(X) - 1  # Index for array X, starting from the end
    j = len(Y) - 1  # Index for array Y, starting from the end

    while i >= 0 and j >= 0:
        if X[i] > Y[j]:
            merged_array.append(X[i])
            i -= 1
        else:
            merged_array.append(Y[j])
            j -= 1

    # Add any remaining elements from X and Y
    while i >= 0:
        merged_array.append(X[i])
        i -= 1

    while j >= 0:
        merged_array.append(Y[j])
        j -= 1

    # Reverse the merged array to get decreasing order
    merged_array.reverse()
    return merged_array

# Example usage:
X = [3, 6, 9]
Y = [2, 4, 7, 8]
result = merge_sorted_arrays_decreasing(X, Y)
print("Merged sorted array in decreasing order:", result)
