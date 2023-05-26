from collections import deque

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    MAX = 9999
    queue = deque()
    queue.append([a, ''])
    visit = [0] * (MAX + 1)
    visit[a] = 1
    while queue:
        x, words = queue.popleft()
        
        if x == b :
            print(words)
            break
        
        dd = 2 * x % 10000
        ds = (x - 1) % 10000
        dl = x // 1000 + (x % 1000) * 10
        dr = x // 10 + (x % 10) * 1000
        if not visit[dd]:
            visit[dd] = 1
            queue.append([dd, words + 'D'])
            
        if not visit[ds]:
            visit[ds] = 1
            queue.append([ds, words + 'S'])
        
        if not visit[dl]:
            visit[dl] = 1
            queue.append([dl, words + 'L'])
            
        if not visit[dr]:
            visit[dr] = 1
            queue.append([dr, words + 'R'])
               
