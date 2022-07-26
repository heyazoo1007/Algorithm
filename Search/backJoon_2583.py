from collections import deque
m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#사각형 있는 곳 채우기(b,a)~(d,c)
for _ in range(k):
    a,b,c,d=map(int,input().split())
    for i in range(b,d):
        for j in range(a,c):
            graph[i][j]=1
            
def bfs(x,y):
    global ans
    queue=deque()
    queue.append([x,y])
    graph[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    queue.append([nx,ny])
                    ans+=1
                    
ans=0
cnt=0
result=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            bfs(i,j)
            cnt+=1
            result.append(ans)
            ans=0
print(cnt)
result.sort()
for i in range(cnt):
    print(result[i]+1,end=' ')
                       
