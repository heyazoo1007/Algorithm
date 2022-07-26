from collections import deque

direction=[[-2,1],[-1,2],[1,2],[2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]

def bfs(a,b,c,d):
    queue=deque()
    queue.append((a,b))
    while queue:
        x,y=queue.popleft()
        if x==c and y==d:
            break        
        for i in range(8):
            nx,ny=x+direction[i][0], y+direction[i][1]
            if 0<=nx<n and 0<=ny<n and not data[nx][ny]:
                data[nx][ny]=data[x][y]+1
                queue.append((nx,ny))
    return data[c][d]

for _ in range(int(input())):
    n=int(input())
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    data=[[0]*(n+1) for _ in range(n+1)]
    data[a][b]=1
    print(bfs(a,b,c,d)-1)
    
