def bfs(x, y, matrix, visit):
    visit[x][y] = 1
    result = [[x, y]]
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and l <= abs(matrix[nx][ny] - matrix[x][y]) <= r:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
                    result.append([nx, ny]) 
    return result
    
n, l, r = map(int, input().split())
matrix = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    
answer = 0
while True:
    flag = False
    visit = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visit[x][y]:
                result = bfs(x, y, matrix, visit)
                # 인구 이동을 할 수 있을 때
                if len(result) >= 2:
                    flag = True
                    total = 0
                    for i, j in result:
                        total += matrix[i][j]
                    temp = total // len(result)
                    for i, j in result:
                        matrix[i][j] = temp
                                       
    if flag == False:
        break
        
    answer += 1
        
print(answer)
