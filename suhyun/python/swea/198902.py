n = int(input())
for i in range(1, n+1):
    s = input()
    if s[::1] == s[::-1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')