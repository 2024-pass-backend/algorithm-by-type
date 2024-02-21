arr = [list(map(int, input().split())) for _ in range(9)]   
max_val = -1
i, j = 0, 0

for row in range(9):
    for col in range(9):
        if arr[row][col] > max_val:
            max_val = arr[row][col]
            i = row
            j = col

print(max_val)
print(i+1, j+1)
        
 