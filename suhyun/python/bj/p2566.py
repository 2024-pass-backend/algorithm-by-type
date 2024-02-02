A = []
max_val = 0
x, y = 0, 0
for i in range(9):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(9):
    for j in range(9):
        if max_val < A[i][j]:
            max_val = A[i][j]
            x = i
            y = j

print(max_val)
print(x+1,y+1)