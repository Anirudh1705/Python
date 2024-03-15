def linear_search(list1, length, key):
    for i in range(length):
        if list1[i] == key:
            return i
    return -1

list1 = [1, 3, 5, 7, 9,15,45,8,6,88,952,254,54,25,484,1545,15485,212,22,]
length = len(list1)
key = 22
result = linear_search(list1, length, key)

if result != -1:
    print("Element found at Index: ", result)
else:
    print("Element not found")