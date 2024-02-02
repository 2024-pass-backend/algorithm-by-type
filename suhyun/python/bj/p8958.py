n = int(input())

for i in range(n):
    sum_val = 0
    v = 0
    word = input()
    for elem in word:
        if elem == 'O':
            v += 1
            sum_val += v
        else:
            v = 0
    print(sum_val)
            
            