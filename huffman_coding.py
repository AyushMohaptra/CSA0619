"""Standalone implementation: 15 Huffman Coding."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def huffman_coding(frequencies):
    heap = []
    serial = 0
    for symbol, frequency in frequencies.items():
        heappush(heap, (frequency, serial, symbol))
        serial += 1
    if not heap:
        return {}
    while len(heap) > 1:
        f1, _, left = heappop(heap)
        f2, _, right = heappop(heap)
        heappush(heap, (f1 + f2, serial, (left, right)))
        serial += 1
    root = heap[0][2]
    codes = {}
    def walk(node, prefix):
        if isinstance(node, tuple):
            walk(node[0], prefix + "0")
            walk(node[1], prefix + "1")
        else:
            codes[node] = prefix or "0"
    walk(root, "")
    return codes

if __name__ == "__main__":
    print("Codes:", huffman_coding({"a": 5, "b": 9, "c": 12, "d": 13}))
