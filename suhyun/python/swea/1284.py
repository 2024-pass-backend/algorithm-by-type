t = int(input())
for tc in range(1, t+1):
    p, q, r, s, w = map(int, input().split())
    a = p * w
    b = q if r >= w else q + (w - r) * s
    # print("a = " + str(a) + "b = " + str(b))
    print(f'#{tc} {min(a,b)}')