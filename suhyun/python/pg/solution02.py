# 대충 만든 자판 (in, not in 키워드)
keymap = ["BC"]
targets = ["AC", "BC"]

def solution(keymap, targets):
    answer = []
    
    for word in targets: #"AC", "BC"
        sum_cnt = 0
        ss = False
        for word_elem in word:
            min_cnt = 101
            for elem in keymap:     # keymap = "BC", word_elem "A"
                if word_elem not in elem:
                    continue
                min_cnt = min(elem.index(word_elem) + 1, min_cnt)
                if min_cnt == 101:
                    ss = True
                    break
            if min_cnt == 101:
                ss = True
                min_cnt = -1
                sum_cnt = 101
                break
            sum_cnt += min_cnt
        if sum_cnt == 101:
            sum_cnt = -1
        answer.append(sum_cnt)
    return answer

solution(keymap, targets)