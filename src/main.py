from collections import deque
import sys

"""
Cache Replacement Policy Simulator

Implements three cache eviction policies:
1. FIFO (First-In First-Out)
2. LRU (Least Recently Used)
3. OPTFF (Belady's Farthest-in-Future)

The program reads an input file containing:
    k m
    r1 r2 r3 ... rm

Where:
    k = cache capacity
    m = number of requests
    r_i = sequence of request IDs

It outputs the number of cache misses for each policy.
"""


def FIFO(k, requests):
    """Return number of misses using FIFO eviction."""
    misses = 0
    q = deque()          # holds items in FIFO order
    in_cache = set()     # fast membership test

    for r in requests:
        if r in in_cache:
            continue  # hit
        misses += 1

        # miss: insert (evict if full)
        if len(q) == k:
            old = q.popleft()
            in_cache.remove(old)

        q.append(r)
        in_cache.add(r)

    return misses


def LRU(k, requests):
    """Return number of misses using LRU eviction."""
    misses = 0
    q = deque()          # left = least recent, right = most recent
    in_cache = set()

    for r in requests:
        if r in in_cache:
            # hit: refresh recency
            q.remove(r)
            q.append(r)
            continue

        # miss
        misses += 1
        if len(q) == k:
            old = q.popleft()
            in_cache.remove(old)

        q.append(r)
        in_cache.add(r)

    return misses


def OPTFF(k, requests):
    """
    Belady's farthest-in-future (optimal offline).
    Evict item whose next use is farthest in the future (or never used again).
    """
    misses = 0
    cache = set()

    # Precompute for each position i, where each item appears next.
    # Build lists of positions for each value.
    positions = {}
    for i, r in enumerate(requests):
        positions.setdefault(r, []).append(i)

    # Pointers into those lists so we can know "next occurrence" quickly
    ptr = {r: 0 for r in positions}

    def next_use(item, current_index):
        """Return the next index > current_index when item is requested, or +inf if never."""
        lst = positions[item]
        p = ptr[item]
        # advance pointer past current_index
        while p < len(lst) and lst[p] <= current_index:
            p += 1
        ptr[item] = p
        if p >= len(lst):
            return float("inf")
        return lst[p]

    for i, r in enumerate(requests):
        # update pointer for r (so next_use works correctly)
        next_use(r, i - 1)  # ensure ptr[r] is at least at current

        if r in cache:
            # hit
            continue

        # miss
        misses += 1

        if len(cache) < k:
            cache.add(r)
            continue

        # cache full: choose eviction victim
        victim = None
        farthest = -1

        for item in cache:
            nu = next_use(item, i)
            if nu > farthest:
                farthest = nu
                victim = item

        cache.remove(victim)
        cache.add(r)

    return misses


def read_input_file(path):
    """
    Input format:
      k m
      r1 r2 r3 ... rm
    """
    with open(path, "r") as f:
        tokens = f.read().split()

    if len(tokens) < 2:
        raise ValueError("Input file must start with: k m")

    k = int(tokens[0])
    m = int(tokens[1])

    req_tokens = tokens[2:]
    if len(req_tokens) < m:
        raise ValueError(f"Expected {m} requests, found {len(req_tokens)}")

    requests = list(map(int, req_tokens[:m]))
    return k, m, requests


def main():
    # Expect: python src/main.py path/to/input.in
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <input_file>")
        sys.exit(1)

    infile = sys.argv[1]
    k, m, requests = read_input_file(infile)

    fifo_misses = FIFO(k, requests)
    lru_misses = LRU(k, requests)
    optff_misses = OPTFF(k, requests)

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {optff_misses}")


if __name__ == "__main__":
    main()