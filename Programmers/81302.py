from collections import deque

def bfs(places, sx, sy):
    queue = deque([(sx, sy)])
    
    visit = [[0] * 5 for _ in range(5)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0 , 1, -1]
    visit[sx][sy] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and (abs(nx - sx) + abs(ny - sy) <= 2) and not visit[nx][ny]:
                if places[nx][ny] == 'P':
                    return False
                if places[nx][ny] == 'O':
                    visit[nx][ny] = 1
                    queue.append((nx,ny))
    return True
    
def solution(places):
    answer = [1] * 5
    
    for t in range(5):
        for i in range(5):
            for j in range(5):
                if places[t][i][j] == 'P':
                    if not bfs(places[t], i, j):
                        answer[t] = 0
                        break
                        
                        
    return answer
