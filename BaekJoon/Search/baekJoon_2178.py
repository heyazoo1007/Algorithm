n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))
    
queue = [[0, 0]]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while queue:
    x, y = queue.pop(0)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])
                
print(matrix[-1][-1])
