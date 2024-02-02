a = [i for i in range(1, 31)]

for i in range(28):
    elem = int(input())
    a.remove(elem)

print(min(a))
print(max(a))
