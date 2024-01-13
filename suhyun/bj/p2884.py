h, m = tuple(map(int, input().split()))

if m < 45:
    if h == 0:
        h = 11
    else: 
        h -= 1
    m += 60
    m -= 45
else:
    m -= 45

print(h, m)
