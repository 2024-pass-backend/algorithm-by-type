t = int(input())

for i in range(1, t+1):
    s = input()
    if s == s[::-1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')