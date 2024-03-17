def insertion_sort(list1):
    for i in range(1, len(list1)):
        key = list1[i]
        j = i - 1
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = key
    return list1

# Test the function
list1 = [5, 8, 1, 6, 3]
print("Original list: ", list1)
print("Sorted list: ", insertion_sort(list1))