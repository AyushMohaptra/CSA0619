"""Standalone implementation: 27 Set Cover Approx."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def set_cover(universe, subsets):
    uncovered = set(universe)
    chosen = []
    remaining = [set(s) for s in subsets]
    while uncovered:
        best = max(remaining, key=lambda s: len(s & uncovered), default=set())
        gain = best & uncovered
        if not gain:
            return None  # supplied subsets cannot cover the universe
        chosen.append(best)
        uncovered -= gain
        remaining.remove(best)
    return chosen

if __name__ == "__main__":
    print("Chosen sets:", set_cover({1, 2, 3, 4}, [{1, 2}, {2, 3}, {3, 4}]))
