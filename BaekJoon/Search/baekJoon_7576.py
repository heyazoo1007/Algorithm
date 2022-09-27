from collections import deque

m,n=map(int,input().split())
data=[]
tomato=deque()
count=0
for i in range(n):
    data.append(list(map(int,input().split())))
    #처음 토마토의 위치 담기
    for j in range(m):
        if data[i][j]==1:
            tomato.append((i,j))
            
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visit=[[0]*m for _ in range(n)]

def bfs():
    while tomato: 
        a,b=tomato.popleft()
        for i in range(4):
            na,nb=a+dx[i],b+dy[i]
            if 0<=na<n and 0<=nb<m:
                if not visit[na][nb] and data[na][nb]==0:
                    visit[na][nb]=1
                    data[na][nb]=data[a][b]+1
                    tomato.append((na,nb))

bfs()
minNum,maxNum=10**9,0

#마지막에는 전체 탐색하면서 0이 있으면 -1, 아니면 최소 일수 출력
for i in range(n):
    if 0 in data[i]:
        minNum=0
    else: 
        maxNum = max(maxNum, max(data[i]))
    
if minNum==0:
    print(-1)
else: 
    print(maxNum-1)
