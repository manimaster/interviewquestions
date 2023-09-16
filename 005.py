# Manikandan Ramanathan (c) 2019
# For a given set of 2 arrays “X” and “Y” consisting of positive integers,
# write a code to find the total number of pairs (x, y) where x is an element of array X
# and y is an element of array Y, and the condition x^y > y^x is satisfied.

def count_pairs_satisfying_condition(X, Y):
    total_pairs = 0
    m = len(X)
    n = len(Y)
    
    # Count the number of 0s and 1s in array Y
    count_zeros = Y.count(0)
    count_ones = Y.count(1)

    # Count pairs where x is 0 or 1
    if count_zeros > 0:
        total_pairs += count_ones

    # Count pairs where x is greater than 1
    for i in range(m):
        if X[i] == 0:
            continue
        if X[i] == 1:
            total_pairs += count_zeros
        else:
            # Count elements in Y such that x^y > y^x
            for j in range(n):
                if Y[j] == 0:
                    continue
                if X[i] > Y[j]:
                    total_pairs += n - j
                else:
                    break

    return total_pairs

# Example usage:
X = [2, 3, 6]
Y = [1, 2]
result = count_pairs_satisfying_condition(X, Y)
print("Total number of pairs satisfying the condition:", result)
