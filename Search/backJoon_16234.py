from collections import deque
import sys 
input=sys.stdin.readline

n,l,r=map(int,input().split())
data=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    data.append(list(map(int,input().split())))
    
def move(result):
    num=0
    for x,y in result:
        num+=data[x][y]
    answer=num//len(result)    
    for x,y in result:
        data[x][y]=answer

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visit[i][j]=1
    result=[]
    result.append([i,j])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                if l <= abs(data[x][y]-data[nx][ny]) <= r:
                    visit[nx][ny]=1
                    queue.append((nx,ny))
                    result.append([nx,ny])
    return result                    
                    
days=0
while True:
    visit=[[0]*n for _ in range(n)]
    isTrue=False
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j]=1
                result=bfs(i,j)
                if len(result)>1:
                    isTrue=True
                    move(result)
    if not isTrue:
        break
    days+=1
    
print(days)                
            
