t = int(input())
for tc in range(1, t+1):
    h1, m1, h2, m2 = tuple(map(int, input().split()))
    m = m1 + m2
    h = 0
    if m >= 60:
        h = m // 60
        m %= 60
    
    h += (h1 + h2)
    if h > 12:
        h -= 12
    
    print(f'#{tc} {h} {m}')
         