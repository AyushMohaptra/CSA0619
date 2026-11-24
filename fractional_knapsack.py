"""Standalone implementation: 14 Fractional Knapsack."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value, selected = 0.0, []
    for weight, value in items:
        if capacity <= 0:
            break
        take = min(1.0, capacity / weight)
        total_value += value * take
        selected.append((weight, value, take))
        capacity -= weight * take
    return total_value, selected

if __name__ == "__main__":
    print("Maximum value:", fractional_knapsack([(10, 60), (20, 100), (30, 120)], 50)[0])
