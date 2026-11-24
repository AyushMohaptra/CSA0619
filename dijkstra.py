"""Standalone implementation: 18 Dijkstra."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def dijkstra(graph, source):
    dist = {v: inf for v in graph}
    for neighbors in graph.values():
        for v, _ in neighbors:
            dist.setdefault(v, inf)
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        current, u = heappop(heap)
        if current != dist[u]:
            continue
        for v, weight in graph.get(u, []):
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights")
            candidate = current + weight
            if candidate < dist[v]:
                dist[v] = candidate
                heappush(heap, (candidate, v))
    return dist

if __name__ == "__main__":
    print("Shortest distances:", dijkstra({0: [(1, 4), (2, 1)], 1: [(2, 2)], 2: [(1, 1)]}, 0))
