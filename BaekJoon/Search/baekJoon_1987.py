n,m=map(int,input().split())
data=[list(input()) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
process=set()
answer=0

def dfs(x,y,count):
    global answer
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if data[nx][ny] not in process:
                process.add(data[nx][ny])
                dfs(nx,ny,count+1)
                process.remove(data[nx][ny])
            else:
                answer=max(answer,count)
                
process.add(data[0][0])
dfs(0,0,1)                
print(answer)
