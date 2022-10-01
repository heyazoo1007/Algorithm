n,m = map(int,input().split())
data = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    data.append(list(input()))

def dfs(x,y,letter,count,sx,sy):
    global flag
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny] and data[nx][ny] == letter:
                visit[nx][ny] = 1
                dfs(nx,ny,letter,count+1,sx,sy)
            elif count >= 4 and sx == nx and sy == ny:
                flag = True
                return          
                
flag = False                                               
for i in range(n):
    for j in range(m):
        sx,sy=i,j
        visit = [[0]*m for _ in range(n)]
        visit[sx][sy] = 1
        dfs(i,j,data[i][j],1,sx,sy)
        if flag:
            print('Yes')
            exit()
        
if not flag:
    print('No')
