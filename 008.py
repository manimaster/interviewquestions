# Manikandan Ramanathan (c) 2019
# For a given array “X” of N positive integers, write a function to return the value “True”
# if a particular triplet (a, b, c) accurately satisfies the condition: a^2 + b^2 = c^2
# (commonly called the Pythagorean Triplet problem).

def has_pythagorean_triplet(X):
    n = len(X)
    X.sort()  # Sort the array in ascending order

    for c in range(n - 1, 1, -1):
        a = 0
        b = c - 1

        while a < b:
            sum_of_squares = X[a] ** 2 + X[b] ** 2

            if sum_of_squares == X[c] ** 2:
                return True
            elif sum_of_squares < X[c] ** 2:
                a += 1
            else:
                b -= 1

    return False

# Example usage:
X = [3, 4, 5, 6, 7]
result = has_pythagorean_triplet(X)
print("Does the array contain a Pythagorean triplet?", result)
