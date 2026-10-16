def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a[1:] if x <= pivot]
    right = [x for x in a[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
a = [5, 3, 8, 1, 2]
print(quick_sort(a))
