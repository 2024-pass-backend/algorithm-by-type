# 프로그래머스 덧칠하기
def solution(n, m, section):
    n_painted, answer = 0, 0
    for s in section:
        if s > n_painted:
            n_painted = s + m - 1
            answer += 1
    return answer