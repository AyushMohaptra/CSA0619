"""Standalone implementation: 24 Hamiltonian Cycle."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def hamiltonian_cycle(graph):
    n = len(graph)
    if n == 0:
        return None
    path = [0]
    def search():
        if len(path) == n:
            return graph[path[-1]][path[0]] != 0
        for vertex in range(1, n):
            if vertex not in path and graph[path[-1]][vertex] != 0:
                path.append(vertex)
                if search():
                    return True
                path.pop()
        return False
    return path + [0] if search() else None

if __name__ == "__main__":
    print("Hamiltonian cycle:", hamiltonian_cycle([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
