n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
def dfs(node, arr, visit):
    visit[node] = 1
    for each in graph[node]:
        if not visit[each]:
            arr.append(each)
            dfs(each, arr, visit)


def bfs(node, arr, visit):
    queue = [node]
    visit[node] = 1
    
    while queue:
        x = queue.pop(0)
        for each in graph[x]:
            if not visit[each]:
                visit[each] = 1
                arr.append(each)
                queue.append(each)

arr_dfs = [v]
visit = [0] * (n + 1)
dfs(v, arr_dfs, visit)

arr_bfs = [v]
visit = [0] * (n + 1)
bfs(v, arr_bfs, visit)

for i in range(len(arr_dfs)):
    print(arr_dfs[i], end = ' ')
print()
for i in range(len(arr_bfs)):
    print(arr_bfs[i], end = ' ')
