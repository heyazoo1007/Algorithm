n, m, k = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(k):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1

def bfs(x, y, matrix, visit):
    queue = [[x, y]]
    visit[x][y] = 1
    count = 1
    
    while queue:
        x, y = queue.pop(0)      
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and matrix[nx][ny] == 1:
                    visit[nx][ny] = 1
                    count += 1
                    queue.append([nx, ny])
    return count 

answer = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and matrix[i][j] == 1:
            answer = max(answer, bfs(i, j, matrix, visit))
            
