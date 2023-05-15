from collections import deque

def move(now):
    data = []
    temp = now
    for _ in range(visit[now] + 1):
        data.append(temp)
        temp = check[temp]        
    print(' '.join(map(str, data[::-1])))
    
    
def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(visit[x])
            move(x)
            return 
        
        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 10 **5 and not visit[nx]:
                visit[nx] = visit[x] + 1
                queue.append(nx)
                check[nx] = x
    
n, k = map(int, input().split())
number = 10 ** 5
visit = [0] * (number + 1)
check
