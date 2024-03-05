import sys
words = set()
for _ in range(int(sys.stdin.readline())):
    words.add(sys.stdin.readline().rstrip())
    
sorted_words = sorted(list(words), key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)