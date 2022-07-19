n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]

def dfs(x,y):
    global count
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0<= ny < n :
            if data[nx][ny] and not visit[nx][ny]:
                visit[nx][ny]=1
                count+=1
                dfs(nx,ny)  
    
visit=[[0]*n for _ in range(n)]                
for i in range(n):
    for j in range(n):
        if not visit[i][j] and data[i][j]==1:  
            visit[i][j]=1
            count=1
            dfs(i,j)
            result.append(count)

            
print(len(result))            
result.sort()
for i in range(len(result)):
    print(result[i])
