t = int(input())

for i in range(1, t+1):
    ans = 0
    a = int(input())
    for j in range(1, a+1):
        if j % 2 == 0:
            ans -= j
        else:
            ans += j
    print(f'#{i} {ans}')    