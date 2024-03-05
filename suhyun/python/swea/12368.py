t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    if a + b > 24:
        print(f'#{tc} {a + b - 24}')
    elif a + b == 24:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {a + b}')
        