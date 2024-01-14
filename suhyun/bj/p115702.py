arr = []

for i in range(10):
    n = int(input())
    arr.append(n % 42)

print(len(set(arr)))