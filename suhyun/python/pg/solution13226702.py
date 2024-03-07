def solution(a, b, n):
    answer = 0
    while(n >= a):
        # 두고 갈 병
        remain_bottle = (n % a)
        # 이제편의점 가서 deal을 해야함
        n = (n // a) * b # >> deal후, 받을 병
        answer += n
        n += remain_bottle ## >> 받을 병과 두고 갈 병을 합쳐서 다음에 편의점으로 오게 하기
    return answer