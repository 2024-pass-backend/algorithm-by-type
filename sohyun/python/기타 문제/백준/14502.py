# 연구소
# 0은 빈 칸, 1은 벽, 2는 바이러스
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
boards = [list(map(int,input().split()))for i in range(N)]

answer = 0
