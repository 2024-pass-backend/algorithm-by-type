money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    print(f'#{t}')
    for i in money:
        if n // i == 0:
            print(0, end=' ')
        else:
            print(n // i, end=' ')
            n %= i
    print()
                
    