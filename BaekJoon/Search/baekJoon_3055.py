n, m = map(int, input().split())
matrix = []
a, b = 0, 0 # 고슴도치 위치 
c, d = 0, 0 # 비버 소굴 위치
queue = []
visit = [[0] * m for _ in range(n)]
for i in range(n):
    matrix.append(list(input()))
    for j in range(m):
        if matrix[i][j] == 'D':
            c, d = i, j
        if matrix[i][j] == 'S':
            a, b = i, j
            visit[i][j] = 1
        if matrix[i][j] == '*':
            queue.append([i, j, 'water'])
            visit[i][j] = -1
            
queue.append([a, b, 'kaktus'])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0
flag = False
while queue:
    x, y, kind = queue.pop(0)
    
    if x == c and y == d:
        if kind == 'kaktus':
            flag = True
            answer = visit[x][y] - 1
            break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny] and (matrix[nx][ny] == '.' or matrix[nx][ny] == 'D'):
                if kind == 'kaktus':
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append([nx, ny, 'kaktus'])
                if kind == 'water':
                    if matrix[nx][ny] == '.':
                        visit[nx][ny] = -1
                        queue.append([nx, ny, 'water'])
                    
if flag == False :
    print('KAKTUS')
else:
    print(answer)
