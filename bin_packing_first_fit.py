"""Standalone implementation: 26 Bin Packing First Fit."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def bin_packing_first_fit(items, capacity):
    bins = []
    for item in items:
        if item > capacity:
            raise ValueError("An item exceeds bin capacity")
        for bin_items in bins:
            if sum(bin_items) + item <= capacity:
                bin_items.append(item)
                break
        else:
            bins.append([item])
    return bins

if __name__ == "__main__":
    print("Bins:", bin_packing_first_fit([4, 8, 1, 4, 2], 10))
