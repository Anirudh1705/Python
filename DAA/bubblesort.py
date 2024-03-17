def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

# Test the function
list1 = [5, 8, 1, 6, 3]
print("Original list: ", list1)
print("Sorted list: ", bubble_sort(list1))