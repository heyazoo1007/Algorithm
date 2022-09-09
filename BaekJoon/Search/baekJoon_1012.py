from collections import deque 

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            na,nb=a+dx[i],b+dy[i]
            if 0<=na<m and 0<=nb<n:
                if not visit[na][nb] and data[na][nb]==1:
                    visit[na][nb]=1
                    queue.append((na,nb))
        
for _ in range(int(input())):
    m,n,k=map(int,input().split())
    data=[[0]*n for _ in range(m)]
    visit=[[0]*n for _ in range(m)]
    count=0
    
    for _ in range(k):
        a,b=map(int,input().split())
        data[a][b]=1
    
    for i in range(m):
        for j in range(n):
            if not visit[i][j] and data[i][j]==1:
                count+=1
                visit[i][j]=1
                bfs(i,j)
    print(count)
