"""Standalone implementation: 20 Kruskal."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def kruskal(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True
    mst, total = [], 0
    for weight, u, v in sorted(edges):
        if union(u, v):
            mst.append((u, v, weight))
            total += weight
    if len(mst) != vertices - 1 and vertices > 0:
        raise ValueError("Graph is disconnected; no spanning tree exists")
    return mst, total

if __name__ == "__main__":
    print("MST and weight:", kruskal(3, [(1, 0, 1), (4, 0, 2), (2, 1, 2)]))
