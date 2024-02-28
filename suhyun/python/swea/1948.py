t = int(input())
mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        print(f'#{tc} {d2}')
    else:
        ans = mon[m1] - d1 + 1
        for i in range(m1+1, m2):
            ans += mon[i]
        ans += d2
        print(f'#{tc} {ans}')
