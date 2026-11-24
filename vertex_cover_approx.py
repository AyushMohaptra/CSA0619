"""Standalone implementation: 28 Vertex Cover Approx."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def vertex_cover_approx(edges):
    uncovered = set()
    cover = set()
    for u, v in edges:
        if u not in cover and v not in cover:
            cover.add(u)
            cover.add(v)
    return cover

if __name__ == "__main__":
    print("Vertex cover:", vertex_cover_approx([(0, 1), (1, 2), (2, 3)]))
