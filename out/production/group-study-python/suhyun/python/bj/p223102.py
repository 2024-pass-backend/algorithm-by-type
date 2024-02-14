n = int(input())
result = 0

for i in range(1, n+1):
    nums = list(map(int, str(i))) #[2, 1, 6]
    result = sum(nums) + i
    
    if result == n:
        print(i)
        break

    if i == n:
        print(0)

# 216을 string화 해준뒤, 이를 리스트화하면, 2 1 6으로 바뀌는 아이디어