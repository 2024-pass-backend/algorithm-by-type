n = int(input())

print(1, end=' ')

for i in range(2, n+1):
    x = str(i)
    clap = x.count('3') + x.count('6') + x.count('9')
    
    if clap == 0:
        print(x, end=' ')
    else:
        print('-' * clap, end=' ')
    
            