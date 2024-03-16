# 카드
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
cards = []
for i in range(N):
    cards.append(int(input()))
cards.sort()
cards_ = Counter(cards).most_common()
print(cards_[0][0])
