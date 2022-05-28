
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def min_max(sequance: list) -> tuple:

    min_val = sequance[0]
    max_val = sequance[0]

    # finding the min value
    for i in range(len(sequance)):
        if sequance[i] < min_val:
            min_val = sequance[i]

    # finding the max value
    for i in range(len(sequance)):
        if sequance[i] > max_val:
            max_val = sequance[i]

    return (min_val, max_val)
