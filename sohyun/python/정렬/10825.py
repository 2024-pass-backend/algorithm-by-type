# 국영수

# 국어 내림차순 x[1]
# 영어 오름차순 x[2]
# 수학 내림차순 x[3]
# 이름 오름차순 x[0]
import sys
input = sys.stdin.readline

N = int(input())
contents = [list(input().split()) for i in range(N)]

contents.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(N):
    print(contents[i][0])
