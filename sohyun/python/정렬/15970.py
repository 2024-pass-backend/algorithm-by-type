# 화살표 그리기
import sys
input = sys.stdin.readline

N = int(input())
dict_ = {}
for i in range(N):
    x,y = map(int, input().split())
    dict_[x] = y
    
result = 0
# color set 구하기
colors = list(set(dict_.values()))
#print(colors)
# color_set 을 for문으로 거리 구하기
for color in colors:
    keys_with_values = [key for key,value in dict_.items() if value == color]
    keys_with_values.sort()
    #print(keys_with_values)
    for i in range(len(keys_with_values)):
        imsi = 0
        if i == 0:
            result += keys_with_values[1] - keys_with_values[0]
            imsi = keys_with_values[1] - keys_with_values[0]
        elif i == len(keys_with_values)-1:
            result += keys_with_values[len(keys_with_values)-1]-keys_with_values[len(keys_with_values)-2]
            imsi = keys_with_values[len(keys_with_values)-1]-keys_with_values[len(keys_with_values)-2]
        else:
            a = keys_with_values[i] - keys_with_values[i-1]
            b = keys_with_values[i+1] - keys_with_values[i]
            result += min(a,b)
            imsi = min(a,b)
        #print(f"{keys_with_values[i]} is {imsi}")
        
print(result)
            
    