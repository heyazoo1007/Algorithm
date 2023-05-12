m, n, k = map(int, input().split())
matrix = [[0] * n for _ in range(m)]
visit = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split()) # 좌표 (x1, y1)은 (m - y1)행 x1열

    for i in range(m - y2, m - y1):
        for j in range(x1, x2):
            matrix[i][j] = 1

def bfs(x, y, visit, matrix):   
    queue = [[x, y]]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 1
    while queue: 
        x, y = queue.pop(0)
        visit[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visit[nx][ny] and matrix[nx][ny] == 0:
                    count += 1
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
    return count    

answer = []
for i in range(m):
    for j in range(n):
        if not visit[i][j] and matrix[i][j] == 0:
            answer.append(bfs(i, j, visit, matrix))
            
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i], end = ' ')
