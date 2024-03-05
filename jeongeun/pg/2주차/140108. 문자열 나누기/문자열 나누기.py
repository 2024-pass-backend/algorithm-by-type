def solution(s):
    ans = 0
    while s:
        x = s[0]
        cnt_x, cnt_other = 0, 0
        for i in range(len(s)):
            if s[i] == x:
                cnt_x += 1
            else:
                cnt_other += 1
            if cnt_x == cnt_other:
                ans += 1
                s = s[i+1:]
                break
        else:
            if cnt_x or cnt_other:
                ans += 1
            break
    return ans