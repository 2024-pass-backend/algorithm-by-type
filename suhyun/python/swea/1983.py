t = int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(1, t+1):
    n, k = tuple(map(int, input().split()))
    data = []
    for j in range(n):
        a, b, c = tuple(map(int, input().split()))
        sum = a * 0.35 + b * 0.45 + c * 0.2
        data.append(sum)
    
    val = data[k-1]
    data.sort(reverse=True)
    
    value = n // 10
    
    print(f'#{i} {score[data.index(val) // value]}')