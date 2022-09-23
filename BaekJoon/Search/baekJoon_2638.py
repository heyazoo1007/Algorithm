import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    queue=deque()
    queue.append((0,0))
    visit[0][0]=1
    while queue :
        x,y=queue.popleft()       
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                if data[nx][ny]>=1:
                    data[nx][ny]+=1
                #공기 면인 경우
                else: 
                    visit[nx][ny]=1
                    queue.append((nx,ny))

time=0
while True:
    visit=[[0]*m for _ in range(n)]
    bfs()
    flag=0
    for i in range(n):
        for j in range(m):
            if data[i][j]>=3:
                data[i][j]=0
                flag=1
            elif data[i][j]==2:
                data[i][j]=1

    if not flag:
        break
    else:
        time+=1
        
print(time)
