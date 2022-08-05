from collections import deque

r,c=map(int,input().split())
data=[]
for _ in range(r):
    data.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visit=[[0]*c for _ in range(r)]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    result=[0,0]
    visit[x][y]=1
    
    if data[x][y]=='o':
        result[0]+=1
    elif data[x][y]=='v':
        result[1]+=1
        
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and not visit[nx][ny]:
                if data[nx][ny]=='.':
                    visit[nx][ny]=1
                    queue.append((nx,ny))
                elif data[nx][ny]=='v':
                    result[1]+=1
                    visit[nx][ny]=1                    
                    queue.append((nx,ny))
                elif data[nx][ny]=='o':
                    result[0]+=1
                    visit[nx][ny]=1
                    queue.append((nx,ny))
    return result

answer=[0,0]                    
for i in range(r):
    for j in range(c):
        if not visit[i][j] and data[i][j]!='#':
            result=bfs(i,j)
            #양이 다 먹히는 경우
            if result[0]<=result[1]:
                answer[1]+=result[1]
            else:
                answer[0]+=result[0]
                
print(answer[0],answer[1])
