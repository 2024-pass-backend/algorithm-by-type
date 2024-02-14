t = int(input())
for i in range(t):
    s = input()
    for j in range(1, 10):
        if s[:j] == s[j:2*j]:
            print(f'#{t} {j}')
            break