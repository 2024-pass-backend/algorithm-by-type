n = int(input())
arr = [25, 10, 5, 1]

for _ in range(n):
    a = int(input())
    for i in range(4):
        mok = a // arr[i]
        a = a % arr[i]
        print(mok, end=' ')
    print()        