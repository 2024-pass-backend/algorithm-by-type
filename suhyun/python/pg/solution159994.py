def solution(cards1, cards2, goal):

    answer = ''
    
    for word in goal:
        include = False
        if cards1:
            if cards1[0] == word:
                include = True
                cards1.pop(0)
        
        if cards2:
            if cards2[0] == word:
                include = True
                cards2.pop(0)
        
        print("1")
        print(cards1)
        print("2")
        print(cards2)
        
        if include == False:
            print("탔음")
            answer = "No"
            break
    
    if include:
        answer = "Yes"
    
    return answer