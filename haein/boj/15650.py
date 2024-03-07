
# backtracking

n, m = list(map(int, input().split()))
sequence = []

def dfs(start):
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, n+1):
        if i not in sequence:
            sequence.append(i)
            dfs(i + 1)
            sequence.pop

dfs(1)
