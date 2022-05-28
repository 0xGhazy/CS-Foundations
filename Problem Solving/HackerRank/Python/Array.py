import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    reversed_array = arr[::-1]
    return numpy.array(reversed_array, float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)