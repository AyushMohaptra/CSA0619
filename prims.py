"""Standalone implementation: 19 Prims."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def prims(graph, start=None):
    if not graph:
        return [], 0
    start = next(iter(graph)) if start is None else start
    visited, heap, mst, total = set(), [], [], 0
    heappush(heap, (0, start, None))
    while heap:
        weight, u, parent = heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if parent is not None:
            mst.append((parent, u, weight))
            total += weight
        for v, w in graph.get(u, []):
            if v not in visited:
                heappush(heap, (w, v, u))
    if len(visited) != len(graph):
        raise ValueError("Graph is disconnected; no spanning tree exists")
    return mst, total

if __name__ == "__main__":
    print("MST and weight:", prims({0: [(1, 1), (2, 4)], 1: [(0, 1), (2, 2)], 2: [(0, 4), (1, 2)]}))
