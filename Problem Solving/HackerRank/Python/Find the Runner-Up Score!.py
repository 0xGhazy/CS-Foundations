

def sortfun(arr):
    new_arr = []
    i = 0
    lowest = arr[0]

    while len(arr) > 0:
        if  arr[i] < lowest:
            lowest = arr[i]
        i += 1
        if i == len(arr):
            new_arr.append(lowest)
            arr.remove(lowest)
            if arr:
                lowest = arr[0]
            i = 0
    return new_arr


def get_runner_up(arr):
    maxval = max(arr)
    test = reversed(arr)
    for i in test:
        if i == maxval or i >= maxval:
            pass
        else:
            return i





arr = []
n = int(input())
test = str(input())
strlist = test.split()
for i in strlist:
    i = int(i)
    arr.append(i)
sorted_list = sortfun(arr)
print(get_runner_up(sorted_list))
