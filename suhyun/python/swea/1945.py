t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = [2, 3, 5, 7, 11]
    arr = [0] * len(nums)
    for i in range(len(nums)):
        cnt = 0
        while(n % nums[i] == 0):
            n //= nums[i]
            cnt += 1
        arr[i] = cnt
    print(f'#{tc}', end = ' ')
    print(*arr)
        
         
            
             