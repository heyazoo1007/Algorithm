from collections import deque
import sys
input = sys.stdin.readline

def solution(T, gears, K, turn):
    for t, direction in turn:
        turnElement = []
        
        # t 기준 오른쪽 기어
        for i in range(t+1, T+1):
            if gears[i][-2] != gears[i-1][2]: 
            	turnElement.append(i)
            else: 
            	break
                
        # t 기준 왼쪽 기어
        for i in range(t-1, 0, -1):
            if gears[i][2] != gears[i+1][-2]: 
            	turnElement.append(i)
            else: 
            	break
                
        # t 기어 회전
        gears[t].rotate(direction)
        
        # t 기어와 맞닿은 극이 다른 기어 회전
        for element in turnElement:
            if (element - t) % 2 != 0 :
                gears[element].rotate(-direction)
            else:
                gears[element].rotate(direction)
            
    return sum([gears[i][0] for i in range(1, T+1)])

T = int(input())
gears = [0] + [deque(map(int,list(input().strip()))) for _ in range(T)]
K = int(input())
turn = [list(map(int, input().split())) for _ in range(K)]

res = solution(T, gears, K, turn)
print(res)
