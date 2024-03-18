# 듣보잡

# version 2 : 이분탐색 이용하기
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
n_people = [input() for i in range(N)]
m_people = [input() for i in range(M)]

n_people.sort()
m_people.sort()

L = 0
answer = []
for i in range(N):
    while L < M:
        if n_people[i] > m_people[L]:
            L += 1
        elif n_people[i] < m_people[L]:
            break
        else:
            answer.append(n_people[i])
            break

print(len(answer))
for com in answer:
    print(com.strip())
# version 1 : intersection 이용하기
'''
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
n_people = [input() for i in range(N)]
m_people = [input() for i in range(M)]

n_set, m_set = set(n_people),set(m_people)
common_ = list(n_set.intersection(m_set))
common_.sort()
print(len(common_))
for com in common_:
    print(com.strip())
'''