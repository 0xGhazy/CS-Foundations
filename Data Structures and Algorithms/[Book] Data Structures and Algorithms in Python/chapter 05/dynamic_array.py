import ctypes                   # for low-level compact array

class DynamicArray:
    
    def __init__(self):
        self._n = 0             # number of elements in the array
        self._capacity = 1      # the max size of elements
        # create new array when i invoke an object from this class
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._n          # return the currant elements number

    def __repr__(self):
        result = ""
        for item in range(self._n):
            if item == self._n - 1:
                result += f"{self._array[item]}"
            else:
                result += f"{self._array[item]}, "
        return f"[{result}]"

    def __getitem__(self, key: int) -> any:
        if  not 0 <= key < self._n:
            raise IndexError(f"The givin index {key} is out of range.")
        else:
            return self._array[key]

    def append(self, element) -> None:
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = element
        self._n += 1

    def _resize(self, new_capacity):
        b = self._make_array(new_capacity)
        for k in range(self._n):
            b[k] = self._array[k]
        self._array = b
        self._capacity = new_capacity

    def _make_array(self, c):
        return (c * ctypes.py_object)()

if __name__ == "__main__":
    my_array = DynamicArray()
    my_array.append(1)
    my_array.append(2)
    my_array.append(3)
    print(my_array)
    