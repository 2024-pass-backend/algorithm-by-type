from itertools import combinations

l, c = map(int, input().split())
li = sorted(list(input().split()))
pwd = combinations(li, l)
sample = 'aeiou'

for c in pwd:
    cnt = 0
    for i in c:
        if i in sample:
            cnt += 1
    if 1 <= cnt <= l - 2:
        print(''.join(c))
