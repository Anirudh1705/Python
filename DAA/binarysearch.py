def binary_search(list1, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if list1[mid] == key:
            return mid
        elif list1[mid] > key:
            return binary_search(list1, low, mid - 1, key)
        else:
            return binary_search(list1, mid + 1, high, key)
    else:
        return -1

list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
key = 11
result = binary_search(list1, 0, len(list1) - 1, key)

if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found")