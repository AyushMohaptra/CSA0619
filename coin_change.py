"""Standalone implementation: 13 Coin Change."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def coin_change(coins, amount):
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)
    return -1 if dp[amount] == inf else dp[amount]

if __name__ == "__main__":
    print("Minimum coins:", coin_change([1, 2, 5], 11))
