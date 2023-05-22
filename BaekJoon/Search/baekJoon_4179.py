from collections import deque

n, m = map(int, input().split())
matrix = []
person = ()
queue = deque()
visit = [[0] * m for _ in range(n)]
for i in range(n):
    matrix.append(list(input()))
    for j in range(m):
        if matrix[i][j] == 'J':
            person = (i, j)
            visit[i][j] = 1
        if matrix[i][j] == 'F':
            queue.append([i, j])
            visit[i][j] = 'F'
queue.append(person)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
check = False
while queue:
    x, y = queue.popleft()
    flag = visit[x][y]
    
    if x in [0, n - 1] or y in [0, m - 1]:
        if flag != 'F':
            check = True
            print(flag)
            break
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] == 0 and (matrix[nx][ny] == '.' or matrix[nx][ny] == '@'):
                if flag == 'F':
                    visit[nx][ny] = flag
                else:
                    visit[nx][ny] = flag + 1
                queue.append([nx, ny])
                
if check == False:
    print('IMPOSSIBLE')
