# 연산자 끼워넣기

import sys
input = sys.stdin.readline

def BT(index, letter,plus,minus,multiply,divide):
    global min_,max_
    if index == N: # 연산자 개수
        min_ = min(letter,min_)
        max_ = max(letter,max_)
        return

    if plus:
        BT(index+1,letter+number[index],plus-1,minus,multiply,divide)
    if minus:
        BT(index+1,letter-number[index],plus,minus-1,multiply,divide)
    if multiply:
        BT(index+1,letter*number[index],plus,minus,multiply-1,divide)
    if divide:
        if letter < 0:
            tot = (-1)*((-1*letter)//number[index])
            BT(index+1,tot,plus,minus,multiply,divide-1)
        else:
            tot = letter // number[index]
            BT(index+1,tot,plus,minus,multiply,divide-1)
                
        

N = int(input())
number = list(map(int,input().split()))
calculation = list(map(int,input().split())) #[+,-,*,/]

min_ = 10**9
max_ = -(10**9)
BT(1,number[0],calculation[0],calculation[1],calculation[2],calculation[3])

print(max_)
print(min_)


