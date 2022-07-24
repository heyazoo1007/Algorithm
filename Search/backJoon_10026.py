from collections import deque

n=int(input())
data=[]
for _ in range(n):
    data.append(list(input()))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
one,two=0,0

def bfs(x,y,letter):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visit[nx][ny] and data[nx][ny]==letter:
                    visit[nx][ny]=1
                    queue.append((nx,ny))
                    
visit=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j,data[i][j])
            one+=1

#적록색약은 적색과 녹색이 같게 보이므로, 둘을 같은 문자로 치환해준다            
for i in range(n):
    for j in range(n):
        if data[i][j]=='R' or data[i][j]=='G':
            data[i][j]='K'
            
visit=[[0]*n for _ in range(n)]            
for i in range(n):
    for j in range(n):
        if not visit[i][j] :
            bfs(i,j,data[i][j])
            two+=1
            
print(one,two)
