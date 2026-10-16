def max_min(a, l, r):
    if l == r:
        return a[l], a[l]
    if r == l + 1:
        return max(a[l], a[r]), min(a[l], a[r])
    m = (l + r) // 2
    max1, min1 = max_min(a, l, m)
    max2, min2 = max_min(a, m + 1, r)
    return max(max1, max2), min(min1, min2)
a = [5, 3, 8, 1, 2]
maximum, minimum = max_min(a, 0, len(a) - 1)
print("Maximum:", maximum)
print("Minimum:", minimum)
