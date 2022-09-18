from collections import deque

n,m=map(int,input().split())
data=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=0
temp=[[0]*m for _ in range(n)]

for i in range(n):
    data.append(list(map(int,input().split())))

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                #data가 아닌 temp임!
                if temp[nx][ny]==0:
                    temp[nx][ny]=2
                    queue.append((nx,ny))

def get_num():
    num=0
    for i in range(n):
        for j in range(m):
            #data가 아닌 temp임!
            if temp[i][j]==0:
                num+=1
    return num 

def dfs(count):
    global answer
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    bfs(i,j)
        answer=max(answer,get_num()) 
        return 
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(answer)
