
N,M = map(int, input().split())
num = list(map(int,input().split()))

#N,M = 4,2
#num = [9,7,9,1]
result = []

def BT(index,letter,visited):
    if index >= M:
        letter_ = ' '.join(map(str,letter))
        result.append(letter_)
        return
    for i in range(N):
        if visited[i] == True: 
            continue
        letter.append(num[i])
        visited[i] = True
        BT(index+1,letter,visited)
        letter.pop()
    return

def BT_(index,letter,visited):
    if index >= M:
        letter_ = ' '.join(map(str,letter))
        result.append(letter_)
        return
    for i in range(N):
        #if i > 0 and num[i] == num[i-1] and not visited[i-1]:
        if visited[i]:
            continue
        letter.append(num[i])
        visited[i] = True
        BT_(index+1,letter,visited)
        visited[i] = False
        letter.pop()
    return 
num = sorted(num)
#BT(0,[],[False]*N)
BT_(0,[],[False]*N)
print("\n".join(result))