# moves순서대로 확인 -> 컬럼의 값이 있을때까지 for문을 돌고, 값이 있다면 바구니에 넣을것
def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        for arr in board:
            if arr[move-1] != 0:
                bucket.append(arr[move-1])
                arr[move-1] = 0
                break
            
        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            answer += 2
            bucket = bucket[:-2]
    
    return answer