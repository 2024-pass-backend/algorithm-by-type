n = int(input())

for i in range(n):
    a, b = input().split()
    for j in b:
        print(int(a) * j, end="")
    print()