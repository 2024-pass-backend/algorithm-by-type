def solution(numbers):
    answer_set = set()
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            answer_set.add(numbers[i] + numbers[j])
    answer = sorted(list(answer_set))
    
    return answer
