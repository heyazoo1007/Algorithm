from collections import deque

n=int(input())
data=[]
count=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    data.append(list(map(int,input().split())))
    
def bfs(x,y,height):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visit[nx][ny] and data[nx][ny]>=height:
                    visit[nx][ny]=1
                    queue.append((nx,ny))
                    
answer=0                    
for x in range(1,100):  
    count=0
    visit=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and data[i][j]>=x:
                count+=1
                bfs(i,j,x)
    answer=max(count,answer)     
    
print(answer)
