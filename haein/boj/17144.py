def calculate_average(numbers):
	if number is None: # 함수에 값이 없으면 종료
    	return None
    if not isinstance(numbers, list): # numbers가 리스트가 아니면 종료
    	return None
    if len(numbers) == 0: # numbers의 길이가 0이면 종료
    	return None
    
    total = sum(numbers)
    average = total/len(numbers)
    return average 
