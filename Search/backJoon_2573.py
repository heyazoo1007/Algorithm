from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(n):
    data.append(list(map(int,input().split())))
    
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visit[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visit[nx][ny] and data[nx][ny]!=0:
                    queue.append((nx,ny))
                    visit[nx][ny]=1
                elif data[nx][ny]==0:
                    ice[x][y]+=1                  
                    
year=0  
flag=False
while True: 
    count=0   
    year+=1
    ice=[[0]*m for _ in range(n)]
    visit=[[0]*m for _ in range(n)]  
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and data[i][j] != 0:
                count+=1
                bfs(i,j)             
    for i in range(n):
        for j in range(m):
            data[i][j]-=ice[i][j]
            if data[i][j]<0:
                data[i][j]=0                
    if count==0:
        break
    if count>1:
        flag=True
        break
        
if flag:
    print(year-1)
else:
    print(0)
