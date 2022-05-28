
# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def manuplate(num1: int, num2: int) -> bool:

    if num1 > num2:
        if num1 % num2 == 0:
            return True
        else:
            return False
    else:
        return False
