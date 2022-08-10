from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = 1
    result = 0
    while queue:
        x = queue.popleft()
        parent = data[x]
        if parent == 0 :
            visit[x] = 1
            result = x 
            break
        if visit[parent]:
            result = parent
            break
        if not visit[parent]:
            visit[parent] = 1
            queue.append(parent)
    return result            
                           
for _ in range(int(input())):
    n = int(input())
    data = [0]*(n+1)    
    for _ in range(n-1):
        a,b = map(int,input().split())      
        data[b] = a
        
    x,y = map(int,input().split())
    visit = [0] * (n+1)
    bfs(x)
    result = bfs(y)
    
    print(result)
