n, m = map(int, input().split())
s = [0] * (n+1)

for i in range(1, n+1):
    s[i] = i

#print(s)

for i in range(m):
    c, d = tuple(map(int, input().split()))
    s[c], s[d] = s[d], s[c]
    #print(s)

for i in range(1, len(s)):
    print(s[i], end=' ')