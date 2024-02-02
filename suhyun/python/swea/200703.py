t = int(input())

for i in range(1, t+1):
    s = input()
    for j in range(1, len(s)):
        if s[:j] == s[j:j*2]:
            print(f'#{i} {j}')
            break