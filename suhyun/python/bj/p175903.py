import sys
l, c = tuple(map(int, sys.stdin.readline().split()))
chars = sorted(sys.stdin.readline().split())
selected = [0] * l
pro(0)

def is_mo(x: str):
    return x in "aeiou"

def pro(x):
    if x == l:
        mo, za = 0, 0
        for x in selected:
            if is_mo(chars[x]):
                mo += 1
            else:
                za += 1
                
        if mo >= 1 and za >= 2:
            for x in selected:
                print(chars[x], end='')
            print()
    
    else:
        st = -1 if k == 0 else selected[k - 1] 
        for i in range(st + 1, c):
            selected[x] = i
            pro(x + 1) 

pro(0)