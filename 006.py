# Manikandan Ramanathan (c) 2019
# For a given array “K,” where all the elements in the array are distinct,
# write a function to find the Kth smallest element where K is a number
# and is smaller than the array’s size.

def kth_smallest_element(K, arr):
    arr.sort()  # Sort the array in ascending order
    if K <= 0 or K > len(arr):
        return None  # K is out of range
    return arr[K - 1]  # Kth smallest element (0-based indexing)

# Example usage:
K = 3
arr = [7, 2, 1, 8, 5, 3, 4, 6]
result = kth_smallest_element(K, arr)
print("The", K, "th smallest element is:", result)
