import sys
n = int(sys.stdin.readline())
ext = [sys.stdin.readline().strip().split(".")[1] for _ in range(n)]
ext.sort()

# [icpc, icpc, icpc, spc, spc, txt,txt, txt, world]
i = 0
while(i < n):
    cnt = 1
    for j in range(i + 1, n):
        if ext[i] == ext[j]:
            cnt += 1
            i += 1
        else:
            break
    print(ext[i], str(cnt))
    i += 1