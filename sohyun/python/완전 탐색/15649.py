def BT(index,letter):
    if index >= M:
        result.append(' '.join(letter))
        return
    for i in range(1,N+1):
        if str(i) not in letter:
            letter.append(str(i))
            BT(index+1,letter)
            letter.pop()
        else:
            continue
    return
result = []    
N,M = map(int,input().split())
BT(0,[])
print("\n".join(result))