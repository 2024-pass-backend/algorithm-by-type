a = [0] * 31

for i in range(28):
    idx = int(input())
    a[idx] = 1

for i in range(1, len(a)):
    if a[i] != 1:
        print(i, end=' ')
