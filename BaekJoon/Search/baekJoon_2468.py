n = int(input())

matrix = []
max_height = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    max_height = max(max_height, max(arr))
    matrix.append(arr)

def bfs(x, y, visit, matrix, rain):
    queue = [[x, y]]
    visit[x][y] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if not visit[nx][ny] and matrix[nx][ny] > rain:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
        
    
answer = 0   
for rain in range(max_height + 1):
    temp = 0 # rain 높이에도 잠기지 않는 영역 
    visit = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visit[x][y] and matrix[x][y] > rain:
                bfs(x, y, visit, matrix, rain)
                temp += 1                
                
    answer = max(answer, temp)    
    
print(answer)
