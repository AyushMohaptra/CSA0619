"""Standalone implementation: 25 Graph Coloring."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n
    def safe(vertex, color):
        return all(not graph[vertex][other] or colors[other] != color
                   for other in range(n))
    def solve(vertex):
        if vertex == n:
            return True
        for color in range(1, m + 1):
            if safe(vertex, color):
                colors[vertex] = color
                if solve(vertex + 1):
                    return True
                colors[vertex] = 0
        return False
    return colors if solve(0) else None

if __name__ == "__main__":
    print("Vertex colors:", graph_coloring([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 3))
