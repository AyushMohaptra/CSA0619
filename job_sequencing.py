"""Standalone implementation: 16 Job Sequencing."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    slots = [None] * (max((d for _, d, _ in jobs), default=0) + 1)
    total_profit = 0
    for job_id, deadline, profit in jobs:
        for slot in range(min(deadline, len(slots) - 1), 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break
    return [job for job in slots[1:] if job is not None], total_profit

if __name__ == "__main__":
    print("Schedule and profit:", job_sequencing([("a", 2, 100), ("b", 1, 19), ("c", 2, 27)]))
