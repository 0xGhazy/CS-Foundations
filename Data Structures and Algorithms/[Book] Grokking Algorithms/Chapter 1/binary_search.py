
def binary_search(my_list: list, item: int) -> int:

    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
        if guess == item:
            return mid
    return None


my_list = [1, 3, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search(my_list, 9))
print(binary_search(my_list, 7000))