from collections import deque
import sys
input=sys.stdin.readline

def bfs(v):
    queue=deque()
    queue.append(v)
    visit[v]=1
    while queue:
        x=queue.popleft()
        for i in data[x]:
            if visit[i] == visit[x]:
                    return False
            elif not visit[i]:
                visit[i]=-visit[x]
                queue.append(i)
    return True            
                
                            
for _ in range(int(input())):
    n,m=map(int,input().split())
    data=[[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b=map(int,input().split())
        data[a].append(b)
        data[b].append(a)

    visit=[0]*(n+1)
    for i in range(1,n+1):
        if not visit[i]: #여기 추가해줘야 틀리지 않는다!           
            flag=bfs(i)   
            if not flag:
                print("NO")
                break       
    if flag:
        print("YES")
         
