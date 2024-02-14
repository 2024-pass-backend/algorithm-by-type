n = int(input())
for _ in range(n):
    cnt, stri = tuple(input().split())
    for x in stri:
        print(int(cnt) * x, end='')
    print()