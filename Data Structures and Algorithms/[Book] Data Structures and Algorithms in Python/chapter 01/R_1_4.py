
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_sq(n: int) -> int:
    total = 0

    for i in range(0, n+1):
        total += i**2
    return total
