s = "aaabbaccccabba"

def solution(s):
    answer = 0  # 분해한 문자열의 개수
    isx, isnotx = 0, 0  # x와 같은 글자 수, 다른 글자 수
    for i in range(len(s)):
        if isx == isnotx:  # 두 횟수가 같으면 분리(answer+1)
            answer += 1
            x = s[i]
            isx, isnotx = 0, 0
            
        if s[i] == x:
            isx += 1
        else:
            isnotx += 1
            
    return answer

print(solution(s))