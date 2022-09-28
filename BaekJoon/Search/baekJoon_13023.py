import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m=map(int,input().split())

data=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

def dfs(v,depth): 
    global flag
    visit[v]=1
    if depth==4:
        flag=True
        return flag
    for x in data[v]:
        if not visit[x]:
            dfs(x,depth+1) 
            visit[x]=0 #여기
    return False   

flag=False
visit=[0]*n #여기           
for i in range(n):
    dfs(i,0)
    visit[i]=0 #여기
    if flag:
        break
if flag:
    print(1)
else:
    print(0)
