n = int(input())

for i in range(1, n+1):
    a = str(i)
    clap = a.count('3') + a.count('6') + a.count('9')

    if clap == 0:
        print(a, end=' ')
    else:
        print('-' * clap, end=' ')         