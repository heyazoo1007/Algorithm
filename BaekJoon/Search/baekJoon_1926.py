from collections import deque

n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
    
visit=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]    
          
def bfs(x,y):
    queue=deque()
    queue.append((x,y))   
    count=1        
    while queue:
           x,y=queue.popleft()
           for i in range(4):
               nx,ny=x+dx[i],y+dy[i]
               if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny] ==0 and data[nx][ny]==1:
                    visit[nx][ny]=1
                    count+=1
                    queue.append((nx,ny))
    return count

result=0
answer=0
for i in range(n):
    for j in range(m):
        if visit[i][j] ==0  and data[i][j]==1:
            visit[i][j]=1
            result=max(result,bfs(i,j))
            answer+=1

print(answer)
print(result)
