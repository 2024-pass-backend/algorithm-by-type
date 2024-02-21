arr = input()
a = 'abcdefghijklmnopqrstuvwxyz'

for i in a:
    if i in arr:
        print(arr.index(i), end=' ')
    else:
        print(-1, end=' ')
    