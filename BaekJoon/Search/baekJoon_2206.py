from collections import deque

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))
    
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1
queue = deque()
queue.append([0, 0, 0])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
flag = False
while queue:
    x, y, isCrash = queue.popleft()
    
    if x == n - 1 and y == m - 1:
        flag = True
        print(visit[x][y][isCrash])
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 0 and not visit[nx][ny][isCrash]:
                visit[nx][ny][isCrash] = visit[x][y][isCrash] + 1
                queue.append([nx, ny, isCrash])
            if matrix[nx][ny] == 1 and isCrash == 0:
                visit[nx][ny][isCrash + 1] = visit[x][y][isCrash] + 1
                queue.append([nx, ny, isCrash + 1])
     

if flag == False:
    print(-1)
