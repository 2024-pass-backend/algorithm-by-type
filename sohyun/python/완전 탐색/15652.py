# N과M(4)
# 비내림차순 = 오름차순

def BT(index,letter,start):
    if index >= M:
        result.append(' '.join(letter))
        return
    for c in range(start, N+1):
        letter.append(str(c))
        BT(index+1,letter,start=c)
        letter.pop()
    return

result,letter = [],[]
N,M = map(int,input().split())
BT(0,[],1)
print("\n".join(result))