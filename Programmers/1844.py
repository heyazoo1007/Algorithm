from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0,0))
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1

    while queue:
        x, y = queue.popleft()   
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and maps[nx][ny] != 0:
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                visit[nx][ny] = 1
                queue.append((nx,ny))
             
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
