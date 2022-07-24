from collections import deque
import sys
input=sys.stdin.readline

n,m,h=map(int,input().split())
data=[[] for _ in range(h)]
tomato=deque()
flag=False

for i in range(h):
    for j in range(m):
        data[i].append(list(map(int,input().split())))
        for k in range(n):
            if data[i][j][k]==1:
                tomato.append((i,j,k))
            if data[i][j][k]==0:
                flag=True
                
direct=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]                

def bfs():
    while tomato:
        a,b,c=tomato.popleft()
        for i in range(6):
            na,nb,nc=a+direct[i][0],b+direct[i][1],c+direct[i][2]
            if 0<=na<h and 0<=nb<m and 0<=nc<n:
                if data[na][nb][nc]==0:                   
                    data[na][nb][nc]=data[a][b][c]+1
                    tomato.append((na,nb,nc))
bfs()

if not flag:
    print(0)
else: 
    minNum,maxNum=10**9,0
    for i in range(h):
        for j in range(m):
            if 0 in data[i][j]:
                minNum=0                
            else: 
                maxNum=max(max(data[i][j]),maxNum)
    if minNum==0:
        print(-1)
    else:
        print(maxNum-1)
