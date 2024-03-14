# 삼총사
def solution(number):
    answer = 0
    number.sort()
    for a in range(len(number)-2):
        for b in range(a+1,len(number)-1):
            for c in range(b+1,len(number)):
                result = number[a]+number[b]+number[c]
                if result == 0:
                    answer += 1
                elif result >0:
                    break
    return answer

# combination 사용
'''
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt
'''