def bubble_sort(arr):
    arr = arr[:]
    n, steps = len(arr), 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            steps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, steps
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {data}\n")
a1, s1 = bubble_sort(data)
print(f"Bubble Sort    O(n^2): {a1}")
