import sys
si = sys.stdin.readline

n, m = map(int, si().split())
a = {}
for i in range(n):
    a[si().strip()] = 0

# print("a")
# print(a)

c = []

for j in range(m):
    name = si().strip()
    # print("name = " + str(name))
    if name in a:
        c.append(name)

c.sort()
print(len(c))
for n in c:
    print(n)
        
        
        
    