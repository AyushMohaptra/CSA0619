def tsp(distance):
    n = len(distance)
    if n == 0:
        return 0, []
    if n == 1:
        return 0, [0, 0]
    dp = {(1, 0): (0, [0])}
    for mask in range(1 << n):
        if not (mask & 1):
            continue
        for last in range(n):
            state = dp.get((mask, last))
            if state is None:
                continue
            cost, path = state
            for nxt in range(1, n):
                if not (mask & (1 << nxt)):
                    new_mask = mask | (1 << nxt)
                    new_cost = cost + distance[last][nxt]
                    old = dp.get((new_mask, nxt))
                    if old is None or new_cost < old[0]:
                        dp[(new_mask, nxt)] = (new_cost, path + [nxt])
    full = (1 << n) - 1
    candidates = [
        (dp[(full, last)][0] + distance[last][0], dp[(full, last)][1] + [0])
        for last in range(1, n) if (full, last) in dp
    ]
    return min(candidates, key=lambda x: x[0])
