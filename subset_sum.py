"""Standalone implementation: 23 Subset Sum."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def subset_sum(numbers, target):
    dp = {0: []}
    for number in numbers:
        for old_sum, subset in list(dp.items()):
            new_sum = old_sum + number
            if new_sum not in dp:
                dp[new_sum] = subset + [number]
        if target in dp:
            return dp[target]
    return dp.get(target)

if __name__ == "__main__":
    print("Subset:", subset_sum([3, 34, 4, 12, 5, 2], 9))
