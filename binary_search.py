def binary_search(a, key):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return -1
a = [1, 3, 5, 7, 9]
key = 7
print(binary_search(a, key))
