words = input().upper() 
# ZZBBA
unique_words = list(set(words))
# ZBA
arr = []
# 2 2 1

for elem in unique_words:
    arr.append(words.count(elem))
    
if arr.count(max(arr)) > 1:
    print('?')
else:
    max_index = arr.index(max(arr))
    print(unique_words[max_index])
    