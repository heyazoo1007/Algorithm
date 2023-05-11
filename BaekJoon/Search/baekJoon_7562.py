import sys
from collections import deque
input = sys.stdin.readline

directions = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]

for _ in range(int(input())):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # [a, b] 에서 [c, d]로 몇 번 만에 가는지 
    
    queue = deque()
    queue.append([a, b])
    visit = [[0] * n for _ in range(n)]
    visit[a][b] = 1 
    while queue:
        x, y = queue.popleft()
        if x == c and y == d:
            break
        
        for i in range(8):
            nx, ny = x + directions[i][0], y + directions[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append([nx, ny])
                    
    print(visit[c][d] - 1)
