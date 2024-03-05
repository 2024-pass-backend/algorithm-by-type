def isValid(s):
    stack = []
    x = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in x.values():
            stack.append(char)
        elif char in x.keys():
            if stack == [] or x[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

def solution(s):
    answer = 0
    for i in range(len(s)):
        if isValid(s[i:] + s[:i]):
            answer += 1
    return answer