def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def main():
    data = [8, 7, 2, 1, 0, 9, 6]
    size = len(data)
    print("Unsorted array:", data)
    quick_sort(data, 0, size - 1)
    print("Sorted array:", data)

if __name__ == "__main__":
    main()