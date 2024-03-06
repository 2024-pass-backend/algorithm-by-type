# 시간초과
n = int(input())
file = dict()
file_extension = []
for i in range(n):
    cnt = 1
    current = input().split(".")[1]
    if current not in file_extension:
        file_extension.append(current)
    if current in file:
        cnt = file[current] + 1
        file[current] = cnt 
    else: file[current] = 1

file_extension.sort()

for i in file_extension:
    print(i, str(file[i]))

  