# 나무 자르기
# 이진 탐색 알고리즘 : start와 end가 같아지는 지점에서 종료될 때 최적의 해를 찾음.

N,M = map(int, input().split())
Tree = list(map(int, input().split()))
Tree.sort(reverse=True) #내림차순

result = 0
R = Tree[0]
L = 1
Mid = int((R+L)/2)

while L <= R:
    
    result = 0
    Mid = (R+L)//2
    
    for tree in Tree:
        if tree > Mid:
            result += (tree-Mid)
    if result < M : # 목표값보다 작음 -> Mid 작아야함.
        R = Mid -1
    else: # 목표값이 큼 -> Mid 커야함.
        L = Mid +1
print(R)
'''
# 알고리즘
 
1) 가장 짧은 길이 1을 start로, 나무 중 가장 긴 길이를 end로 둔다.
2) 이분탐색이 끝날 때까지 while 문을 돌린다.
3) mid를 start와 end의 중간으로 두고, 모든 값에서 mid를 빼 총 어느정도 길이의 벌목된 나무가 나오나 살펴본다.
4-1) 벌목나무가 목표치 이상이면 mid+1을 start로 두고 다시 while문 반복
4-2) 벌목나무가 목표치 이하면 mid-1을 end로 두고 다시 while문 반복
5) start와 end가 같아지면: 조건을 만족하는 최대의 나무 절단 높이를 찾으면 탈출한다.★★★
6) 결과값인 end출력
'''