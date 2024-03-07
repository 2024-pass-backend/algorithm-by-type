def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    apple_box = []
    for i in range(0, len(score), m):
        apple_box.append(score[i:i+m])
    for apple in apple_box:
        if len(apple) == m:
            answer += min(apple) * m ## min(apple) ? 
    
    return answer

score = [1, 2, 3, 1, 2, 3, 1]
solution(3, 4, score)