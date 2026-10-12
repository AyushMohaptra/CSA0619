def selection_sort(arr):
    arr = arr[:]
    n, steps = len(arr), 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, steps
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {data}\n")
a2, s2 = selection_sort(data)
print(f"Selection Sort O(n^2): {a2}")
