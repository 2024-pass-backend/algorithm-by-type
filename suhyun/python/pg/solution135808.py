# 8:27 ~ 
# 일단 정렬을 해야하나? 완탐치고는 최댓값이 굉장히 큼
# 정렬 = 십만log십만
def solution(k, m, score):  # [3, 3, 2, 2, 1, 1, 1]
    score.sort(reverse=True) # [3, 3, 2, 2, 1, 1, 1]
    ## 구해야하는 묶음 갯수
    select = len(score) // m
    answer = 0
    i, j = 0, 0
    while(i < len(score)):
        a = []
        min_value = 9
        while(len(a) < m and j < len(score)): 
            a.append(score[j])
            j += 1
        if len(a) == m:
            min_value = min(a)
        i = j
        answer += (min_value * m * 1) 
        
    return answer

score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(4, 3, score))