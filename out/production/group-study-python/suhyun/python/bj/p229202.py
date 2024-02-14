n = int(input())
pipe, cnt = 1, 1

while n > pipe:
    pipe += cnt * 6
    cnt += 1

print(cnt)