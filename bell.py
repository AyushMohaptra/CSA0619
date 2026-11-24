def bellman_ford(vertices, edges, source):
    dist = [inf] * vertices
    dist[source] = 0
    for _ in range(vertices - 1):
        changed = False
        for u, v, weight in edges:
            if dist[u] != inf and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                changed = True
        if not changed:
            break
    for u, v, weight in edges:
        if dist[u] != inf and dist[u] + weight < dist[v]:
            raise ValueError("Reachable negative-weight cycle detected")
    return dist
