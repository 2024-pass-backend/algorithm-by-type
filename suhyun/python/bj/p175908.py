l, c = map(int, input().split())
chars = sorted(input().split())
selected = [0] * l

def is_mo(x: str):
    return x in "aeiou"
    
def pro(idx):
    if idx == l:
        mo, za = 0, 0
        for c in selected:
            if is_mo(chars[c]):
                mo += 1
            else:
                za += 1
        
        if mo >= 1 and za >= 2:
            for c in selected:
                print(chars[c], end='')
            print()
    
    else:
        start = 0 if idx == 0 else selected[idx-1] + 1
        for cand in range(start, len(chars)):
            # print("idx = " + str(idx))
            selected[idx] = cand
            pro(idx + 1)
        
pro(0)


