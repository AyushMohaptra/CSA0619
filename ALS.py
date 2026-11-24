def activity_selection(activities):
    activities = sorted(activities, key=lambda x: x[1])
    chosen, last_finish = [], -inf
    for start, finish in activities:
        if start >= last_finish:
            chosen.append((start, finish))
            last_finish = finish
    return chosen
