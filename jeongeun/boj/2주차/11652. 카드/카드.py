import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(N)]
counter = Counter(cards)

max_count = counter.most_common(1)[0][1]
most_common = min(k for k, v in counter.items() if v == max_count)

print(most_common)
