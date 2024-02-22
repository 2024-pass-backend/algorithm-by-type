n = int(input())

for i in range(1, n+1):
    a = input()
    for j in range(1, len(a)):
        if a[:j] == a[j:j*2]:
            print(f'#{i} {j}')
            break
 