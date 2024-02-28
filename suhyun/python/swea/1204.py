t = int(input())
for tc in range(1, t+1):
    n = int(input())
    score = [0] * 101
    arr = map(int, input().split())
    mode = 0
    for elem in arr:
        score[elem] += 1
        if score[elem] >= score[mode]:
            mode = elem
    print(f'#{tc} {mode}')
        
    