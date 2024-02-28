def is_mo(x: str):
    return x in "aeiou"

def pro(x):
    if x == l:
        mo, za = 0, 0
        for s in selected:
            if is_mo(chars[s]):
                mo += 1
            else:
                za += 1

        if mo >= 1 and za >= 2:
            for s in selected:
                print(chars[s], end='')
            print()
    else:
        st = -1 if x == 0 else selected[x - 1]
        for i in range(st + 1, c):
            selected[x] = i
            pro(x + 1)

import sys
l, c = tuple(map(int, sys.stdin.readline().split()))
chars = sorted(sys.stdin.readline().split())
selected = [0] * l
pro(0)