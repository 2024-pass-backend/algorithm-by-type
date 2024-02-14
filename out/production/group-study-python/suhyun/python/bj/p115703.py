words = input().upper()
unique_words = list(set(words))

# ZA
# 2 1

arr = []

for elem in unique_words:
    arr.append(words.count(elem))

if arr.count(max(arr)) > 1:
    print('?')
else:
    idx = arr.index(max(arr))
    print(unique_words[idx])
    