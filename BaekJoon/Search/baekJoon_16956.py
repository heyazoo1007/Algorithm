from collections import deque

n,m = map(int,input().split())
data = [list(map(int, input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
answer = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,itr):    
    visit[x][y] = itr
    queue=deque()
    queue.append((x,y))
    count = 1
    temp = []
    while queue: 
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] != itr:
                #0인 경우
                if not data[nx][ny] :  
                    visit[nx][ny] = itr
                    #0의 갯수 세기
                    count += 1
                    queue.append((nx,ny))
                #1인 경우
                else: 
                    temp.append([nx,ny])
                    visit[nx][ny] = itr
    for i,j in temp:
        answer[i][j] += count
        
for i in range(n):
    for j in range(m):
        if data[i][j]:
            answer[i][j] = 1
itr = 1            
for i in range(n):
    for j in range(m):
        #방문하지 않았고, 0인 위치에 대해서 bfs 진행
        if not data[i][j] and not visit[i][j]:
            bfs(i,j,itr)
            itr += 1
            
for i in range(n):
    for j in range(m):
        print(answer[i][j] % 10, end='')
    print()
