from collections import deque

def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue : 
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and matrix[nx][ny] == 0:
                    visit[nx][ny] = 1
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])
                    
        
m, n = map(int, input().split())
matrix = []
queue = deque()
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])


visit = [[0] * m for _ in range(n)]
bfs()
            
answer = 0
flag = True
for i in range(n):
    if 0 in matrix[i]:
        flag = False
        break
    else:
        answer = max(answer, max(matrix[i]))
        
if flag == True:    
    print(answer - 1)
else:
    print(-1)
            
