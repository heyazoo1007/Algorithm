from collections import deque
n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input())))
visit=[[0]*m for _ in range(n)]    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    visit[x][y]=1
    queue=deque()
    queue.append((x,y))
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            na,nb=a+dx[i],b+dy[i]
            if 0<=na<n and 0<=nb<m:
                if not visit[na][nb] and data[na][nb]==1:
                    visit[na][nb]=visit[a][b]+1
                    queue.append((na,nb))
bfs(0,0)
print(visit[-1][-1])
