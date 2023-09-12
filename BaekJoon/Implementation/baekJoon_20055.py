from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
answer = 0

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    
    if sum(robot): #로봇이 존재할 때
        for i in range(n - 2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0: # 다음 칸에 로봇 없고
                if belt[i + 1] >= 1 : #벨트 내구성 1이상
                    robot[i + 1] = 1
                    robot[i] = 0
                    belt[i + 1] -= 1
        robot[-1] = 0 # 맨 마지막에 있는 박스 내림 
        
    if robot[0] == 0 and belt[0] >= 1 : # 올리는 위치에 로봇 없고, 내구성 1이상
        robot[0] = 1
        belt[0] -= 1
    
    answer += 1
    if belt.count(0) >= k:
        break

print(answer)
                
