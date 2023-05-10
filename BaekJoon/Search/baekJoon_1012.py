import sys
input = sys.stdin.readline

def bfs(x, y, visit):
    queue = [[x, y]]
    visit[x][y] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visit[nx][ny] and matrix[nx][ny] == 1:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
        
    
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    matrix = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        matrix[a][b] = 1
        
    visit = [[0] * n for _ in range(m)]  
    answer = 0 
    for i in range(m):
        for j in range(n):
            if not visit[i][j] and matrix[i][j] == 1:
                answer += 1
                bfs(i, j, visit)
                
    print(answer)
