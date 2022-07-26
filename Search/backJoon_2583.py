from collections import deque

m,n,k=map(int,input().split())
data=[[0]*n for _ in range(m)]
visit=[[0]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]
def change(a,b,c,d):
    for i in range(m-d,m-b):
        for j in range(a,c):
            data[i][j]=1
for _ in range(k):
    a,b,c,d=map(int,input().split())
    change(a,b,c,d)

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    global result
    count=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if not visit[nx][ny] and not data[nx][ny]:
                    visit[nx][ny]=1
                    count+=1 #너무 복잡하게 생각함 
                    queue.append((nx,ny)) #bfs의 기본 중 기본을 빼먹음
    result.append(count)
    
for i in range(m):
    for j in range(n):
        if not visit[i][j] and not data[i][j]:
            visit[i][j]=1
            bfs(i,j)
            #count=1 #count가 gloabl이라 계속 초기값 설정해줘야 함
            
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i], end =' ')
                   
