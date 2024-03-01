# 대충 만든 자판 (in, not in 키워드)
keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]

def solution(keymap, targets):
    answer = []
    
    for word in targets: #"ABCD", "AABB"
        cnt = 0
        for word_elem in word:
            min_cnt = 101
            for elem in keymap:     # elem = "ABACD"
                if word_elem not in elem:
                    continue
                min_cnt = min(elem.index(word_elem), min_cnt)
            if min_cnt == 101: 
                cnt = -1
        answer.append(cnt)