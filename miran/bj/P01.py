import sys
input = sys.stdin.readline
n,m=map(int,input().split())
ans=[]

def checking(ans):
    if len(ans)==m:
        print(*ans)
    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
            checking(ans)
            ans.pop()

checking(ans)
