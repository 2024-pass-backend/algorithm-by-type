dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
sum = 0

for x in s:
    for elem in dial:
        if x in elem:
            sum += dial.index(elem) + 3 

print(sum)    

