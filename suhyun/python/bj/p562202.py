dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sum = 0

for x in range(len(a)):
    for elem in dial:
        if a[x] in elem:
            sum += dial.index(elem)+3

print(sum)