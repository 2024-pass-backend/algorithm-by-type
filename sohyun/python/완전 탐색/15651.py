# N과 M(3)

# backtracking
def BT(index,letter):
    if index >= M:
        result.append(' '.join(letter))
        return
    for c in range(1,N+1):
        letter.append(str(c))
        BT(index+1,letter)
        letter.pop()  # line 10 [1,2,3]인 경우, 마지막 숫자를 제거한 [1,2]로 되돌리기 위함.
    return

result,letter = [],[]
N,M = map(int,input().split())
BT(0,[])
print("\n".join(result))


# 내장함수 사용하기
'''
from itertools import permutations
N,M = map(int, input().split())
p = permutations(range(1,N+1),M)
for i in p:
    print(" ".join(map(str,i)))
'''