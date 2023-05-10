n = int(input())
first, second = map(int, input().split()) 
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 여기 추가 안 해서 틀림

queue = [[first, 0]]
visit = [0] * (n + 1)
visit[first] = 1
answer = -1
while queue:
    person, level = queue.pop(0)
    
    if person == second:
        answer = level
        break
    
    for each in graph[person]:
        if not visit[each]:
            visit[each] = 1
            queue.append([each, level + 1])

print(answer)
