from collections import deque

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)] #여기 n+1로 하기

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort() #여기
    graph[b].sort() #여기 추가하기 안그럼 11%에서 틀림

def dfs(x):
    visit[x]=1 #시작할 때 방문 처리
    print(x, end = ' ') #이런식으로 출력하기 
    for i in graph[x]: #range(graph[x]) 아님
        if not visit[i]:
            dfs(i)

def bfs(x):
    queue=deque()
    queue.append(x)
    visit[x]=1
    while len(queue)>0:
        a=queue.popleft()
        print(a, end = ' ')
        for i in graph[a]:
            if not visit[i]:
                visit[i]=1
                queue.append(i)
                
visit=[0]*(n+1) 
dfs(v)
print()
visit=[0]*(n+1) 
bfs(v)
