from collections import deque

r,c=map(int,input().split())
data=[]
visit=[[0]*c for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=deque()

for i in range(r):
    data.append(list(input()))
    for j in range(c):
        if data[i][j]=='S':
            queue.append((i,j))
        elif data[i][j]=='D':
            Dx,Dy=i,j
            
for i in range(r):
    for j in range(c):
        if data[i][j]=='*':
            queue.append((i,j))
            
#고슴도치가 S, 목적지가 D
def bfs(Dx,Dy):
    while queue:
        x,y=queue.popleft()
        #목적지에 고슴도치가 도착해있는 경우 
        if data[Dx][Dy]=='S':
            #이동한 최단거리 반환 
            return visit[Dx][Dy]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<= nx < r and 0<= ny < c:
                #고슴도치는 비어있거나, 굴인 경우에만 이동할 수 있다 
                if data[x][y]=='S' and (data[nx][ny]=='.' or data[nx][ny]=='D'):
                    data[nx][ny]='S'
                    visit[nx][ny]=visit[x][y]+1
                    queue.append((nx,ny))
                #물은 비어있거나, 고슴도치인 경우에만 이동할 수 있다 
                elif data[x][y]=='*' and (data[nx][ny]=='.' or data[nx][ny]=='S'):
                    data[nx][ny]='*'
                    queue.append((nx,ny))
    return 'KAKTUS'

print(bfs(Dx,Dy))
