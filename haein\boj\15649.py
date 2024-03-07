'''
  # back tracking
  - 가능성 없는 곳에선 되돌아가고(백트랙킹) 가능성 있는 곳을 탐색
  - 보통 재귀로 구현
  - 완탐과 다름, 완탐은 모든 경우의 수를 탐색하는 방법으로 백트랙킹이 더 효율적이다.
'''

n, m = map(int, input().split())

sequence = [] # m개 수열 저장하기 위한 리스트

def dfs():
    if len(sequence) == m: # 리스트에 들어간 수열이 m개가 되면 리스트의 숫자들을 출력하고 함수 빠져나오기
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, n + 1): # 1부터 n까지 숫자들 모두 확인
        if i not in sequence: # n까지 숫자가 sequence에 없다면 
            sequence.append(i) # 추가
            dfs() # 재귀
            sequence.pop
