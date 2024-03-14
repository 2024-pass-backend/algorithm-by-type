# 가장 많이 받은 선물

def solution(friends, gifts):
    gift_counts = [[0 for i in range(len(friends))] for j in range(len(friends))]
    
    for gift in gifts:
        giveG = gift.split(' ')[0]
        receiveG = gift.split(' ')[1]
        gift_counts[friends.index(giveG)][friends.index(receiveG)] += 1
    
    # dict{준, 받은, 선물지수}
    gift_dict = {}
    for i in range(len(friends)):
        GivenGifts = sum(gift_counts[i][:])
        ReceiveGifts = 0
        for k in range(len(friends)):
            ReceiveGifts += gift_counts[k][i]
        ResultGifts = GivenGifts - ReceiveGifts
        gift_dict[friends[i]] = {
            'give':GivenGifts,
            'receive':ReceiveGifts,
            'result':ResultGifts
        }
    gifts_next_month = [0 for i in range(len(friends))]
    
    for i in range(len(friends)-1):
        for k in range(i,len(friends)):
            # 준 & 받은 비교
            firstPeople = gift_counts[i][k]
            secondPeople = gift_counts[k][i]
            if firstPeople > secondPeople:
                gifts_next_month[i] += 1
            elif firstPeople < secondPeople:
                gifts_next_month[k] += 1
            else: # 같거나 없거나
                firstPeopleResult = gift_dict[friends[i]]['result']
                secondPeopleResult = gift_dict[friends[k]]['result']
                if firstPeopleResult > secondPeopleResult:
                    gifts_next_month[i] += 1
                elif firstPeopleResult < secondPeopleResult:
                    gifts_next_month[k] += 1
    return max(gifts_next_month)

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(friends,gifts))