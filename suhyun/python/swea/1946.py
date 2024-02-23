t = int(input())
for tc in range(1, t+1):
    n = int(input())
    str = ''
    for i in range(n):
        alpha, nums = tuple(input().split())
        nums = int(nums)
        str += (alpha * nums)
    
    print(f'#{tc}')
    for i in range(0, len(str), 10):
        print(str[i:i+10])
        
        