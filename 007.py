# Manikandan Ramanathan (c) 2019
# You’re given an array “X” of size “N,” containing sets of 0s, 1s, and 2s.
# Write a program to sort the array elements in ascending order.

def sort_array_of_0s_1s_2s(X):
    low, mid, high = 0, 0, len(X) - 1

    while mid <= high:
        if X[mid] == 0:
            X[low], X[mid] = X[mid], X[low]
            low += 1
            mid += 1
        elif X[mid] == 1:
            mid += 1
        else:
            X[mid], X[high] = X[high], X[mid]
            high -= 1

# Example usage:
X = [0, 1, 2, 1, 0, 2, 1, 0]
sort_array_of_0s_1s_2s(X)
print("Sorted array:", X)
