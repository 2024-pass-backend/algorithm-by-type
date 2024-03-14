# 세번째 시도 : 두번째 시도의 간결 버전
def solution(players, callings):
    answer = players
    running = {key:i for i,key in enumerate(players)}

    for calling in callings:
        calling_rank = running.get(calling) # rank
        
        running[calling] -= 1
        running[answer[calling_rank-1]] += 1
        
        answer[calling_rank],answer[calling_rank-1] =  answer[calling_rank-1], answer[calling_rank]
    return answer
players = ["mumu", "soe", "poe", "kai", "mine"]
calling = ["kai", "kai", "mine", "mine"]
print(solution(players=players,callings=calling))


'''
# 두번째 시도 : 성공
def solution(players, callings):
    answer = players
    running = {}
    for i in range(len(players)):
        running[players[i]] = i+1
        
    for calling in callings:
        calling_rank = running.get(calling) # rank
        called_name = players[int(calling_rank)-2]
        
        running[calling] = calling_rank-1
        running[called_name] = calling_rank
        answer[calling_rank-1]= called_name
        answer[calling_rank-2] = calling
    return answer
'''

'''
# 첫번쨰 시도 : 시간 초과
# 원인 : called_name_list = [key for key,value in running.items() if value==calling_race-1]
def solution(players, callings):
    answer = []
    running = {}
    for i in range(len(players)):
        running[players[i]] = i+1
        
    for calling in callings:
        calling_race = running.get(calling) # rank
        called_name_list = [key for key,value in running.items() if value==calling_race-1]
        called_name = ''.join(called_name_list)
        running[called_name] = calling_race
        running[calling] = calling_race -1
    running_sorted = sorted(running.items(), key=lambda item:item[1])
    for i in range(len(running_sorted)):
        answer.append(running_sorted[i][0])
    return answer

'''