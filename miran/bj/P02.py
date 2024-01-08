n,m=map(int,input().split())
visit=[0]*(n+1)
ans=[]


def find(ans):
    if len(ans)==m:
        for i in ans:
            print(i,end=" ")
        print()
        return
    for i in range(1,n+1):
        ans.append(i)
        find(ans)
        ans.pop()

find(ans)