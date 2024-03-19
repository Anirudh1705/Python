def selection_sort(list1):
    for i in range(len(list1)):
        min_index = i
        for j in range(i+1, len(list1)):
            if list1[min_index] > list1[j]:
                min_index = j
        list1[i], list1[min_index] = list1[min_index], list1[i]
    return list1

# Test the function
list1 = [5, 8, 1, 6, 3]
print("Original list: ", list1)
print("Sorted list: ", selection_sort(list1))