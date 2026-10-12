def insertion_sort(arr):
    arr = arr[:]
    n, steps = len(arr), 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            steps += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr, steps
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {data}\n")
a3, s3 = insertion_sort(data)
print(f"Insertion Sort O(n^2): {a3}")
