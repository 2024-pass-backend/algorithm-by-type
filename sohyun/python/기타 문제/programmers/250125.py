def solution(board, h, w):
    answer = 0
    dh = [1,-1,0,0]
    dw = [0,0,1,-1]
    n = len(board[0])
    
    color = board[h][w]
    for i in range(len(dh)):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if (0<=h_check<n) and (0<=w_check<n):
            if board[h_check][w_check] == color:
                answer += 1
    return answer

board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1
print(solution(board,h,w))