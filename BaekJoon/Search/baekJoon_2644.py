from collections import deque 

n = int(input())
x, y = map(int,input().split())
m = int(input())
data = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
    
def bfs(x,y):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        if x == y:
            return visit[y]
        for i in data[x]:
            if not visit[i]:
                queue.append(i)
                visit[i] = visit[x]+1
    return -1        

print(bfs(min(x,y),max(x,y)))    

    
