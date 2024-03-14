# 키패드 자체를 딕셔너리로, 번호는 key, 그에 해당하는 1차원 좌표는 value
def solution(numbers, hand):
    answer = ''
    pad = {
        "1":(0,0), "2":(0,1), "3":(0,2),
        "4":(1,0), "5":(1,1), "6":(1,2),
        "7":(2,0), "8":(2,1), "9":(2,2),
        "*":(3,0), "0":(3,1), "#":(3,2)
    }
    
    left = pad['*']
    right = pad['#']
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = pad[str(num)]
        
        elif num in [3, 6, 9]:
            answer += 'R'
            right = pad[str(num)]
        
        else:
            # 2, 5, 8, 0일때, 왼손과 오른손의 거리비교, 왼손과 번호까지의 거리 = |x좌표의 차| + |y좌표의 차|
            left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
            right_dis = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])
            
            # 오른손이 더 가까울때
            if left_dis > right_dis:
                right = pad[str(num)]
                answer += "R"
            # 왼손이 더 가까울때 
            elif left_dis < right_dis:
                left = pad[str(num)]
                answer += "L"
            else:
                if hand == "right":
                    right = pad[str(num)]
                    answer += "R"
                else:
                    left = pad[str(num)]
                    answer += "L"
    
    return answer