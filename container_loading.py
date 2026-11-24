"""Standalone implementation: 17 Container Loading."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def container_loading(weights, capacity):
    chosen, total = [], 0
    for weight in sorted(weights):
        if total + weight <= capacity:
            chosen.append(weight)
            total += weight
    return chosen, total

if __name__ == "__main__":
    print("Loaded containers and total:", container_loading([4, 8, 1, 4, 2], 10))
