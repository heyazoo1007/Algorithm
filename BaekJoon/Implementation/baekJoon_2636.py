from collections import deque

def bfs():
    queue = deque() # 값이 0인 좌표
    queue.append([0, 0])
    melt = deque()  # 가장 바깥에 있는 치즈 좌표
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] :
                visit[nx][ny] = 1
                if cheese[nx][ny] == 0:
                    queue.append([nx, ny])
                elif cheese[nx][ny] == 1:
                    melt.append([nx, ny])
    for x, y in melt:
        cheese[x][y] = 0
    return len(melt)
                
    
n, m = map(int, input().split())

cheese = []
count = 0 # 나중에 모두 없어지기 한 시간 전 치즈 칸 개수 세기 위함
time = 1
for i in range(n):
    data = list(map(int, input().split()))
    cheese.append(data)
    for j in range(m):
        if data[j] == 1:
            count += 1   

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while True:
    visit = [[0] * m for _ in range(n)]
    melt_count = bfs()
    count -= melt_count
    if count == 0:
        print(time)
        print(melt_count)
        break
    time += 1
        

