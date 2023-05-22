from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n = map(int, input().split())
    matrix = []
    queue = deque()
    start = ()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [[-1] * m for _ in range(n)]
    for i in range(n):
        matrix.append(list(input()))
        for j in range(m):
            if matrix[i][j] == '*':
                visit[i][j] = 'FIRE'
                queue.append([i, j])
            if matrix[i][j] == '@':
                visit[i][j] = 0
                start = (i, j)
    queue.append(start)
   
    check = False
    while queue:
        x, y = queue.popleft()
        
        if visit[x][y] != 'FIRE':
            flag = visit[x][y]
        else:
            flag = 'FIRE'
            
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            if flag != 'FIRE':
                check = True
                print(flag + 1)
                break
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == -1 and (matrix[nx][ny] == '.' or matrix[nx][ny] == '@'):
                    if flag == "FIRE":
                        visit[nx][ny] = flag
                    else:
                        visit[nx][ny] = flag + 1
                    queue.append([nx, ny])
                    
    if check == False:
        print('IMPOSSIBLE')
                                 
    
