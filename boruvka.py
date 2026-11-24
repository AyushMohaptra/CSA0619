"""Standalone implementation: 21 Boruvka."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def boruvka(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True
    mst, total, components = [], 0, vertices
    while components > 1:
        cheapest = {}
        for weight, u, v in edges:
            ru, rv = find(u), find(v)
            if ru != rv:
                if ru not in cheapest or weight < cheapest[ru][0]:
                    cheapest[ru] = (weight, u, v)
                if rv not in cheapest or weight < cheapest[rv][0]:
                    cheapest[rv] = (weight, u, v)
        if not cheapest:
            break
        for weight, u, v in cheapest.values():
            if union(u, v):
                mst.append((u, v, weight))
                total += weight
                components -= 1
    if components > 1:
        raise ValueError("Graph is disconnected; no spanning tree exists")
    return mst, total

if __name__ == "__main__":
    print("MST and weight:", boruvka(3, [(1, 0, 1), (4, 0, 2), (2, 1, 2)]))
