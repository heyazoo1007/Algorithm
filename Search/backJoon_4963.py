from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx,ny=x+direct[i][0],y+direct[i][1]            
            if 0<=nx<h and 0<=ny<w:
                if not visit[nx][ny] and data[nx][ny]==1:
                    visit[nx][ny]=1
                    queue.append((nx,ny))
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    data=[]
    for _ in range(h):
        data.append(list(map(int,input().split())))
    #방향 때문에 엄청 틀렸네,,,,
    direct=[[1,1],[-1,1],[1,-1],[-1,-1],[0,-1],[0,1],[1,0],[-1,0]]
    count=0
    visit=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and data[i][j]==1:
                visit[i][j]=1
                count+=1
                bfs(i,j)
                
    print(count)
