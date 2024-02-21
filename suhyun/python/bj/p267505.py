n = int(input())
for i in range(n):
    a, b = input().split()
    for i in b:
        print(int(a) * i, end='')
    print()