t = int(input())
for i in range(1, t+1):
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')
    
    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end=' ')

j = 1
print(1 == '3')