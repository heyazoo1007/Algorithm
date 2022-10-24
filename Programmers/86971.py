def connect(arr, i, graph):
    stack = []
    for i in arr:
        stack.append(i)
        
    visit = [0] * (len(graph) + 1)
    visit[0], visit[i] = 1, 1
    
    while stack:
        a = stack.pop()
        for i in graph[a]:
            if not visit[i]:
                stack.append(i)
                visit[i] = 1
                
    return visit

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
    min_num = 100
    for i in range(1, n + 1):
        for j in range(len(graph[i])):
            temp = graph[i][j]
            graph[i].remove(graph[i][j])
            if graph[i]:
                result = connect(graph[i], i, graph)
                min_num = min(min_num, abs(result.count(0) - result.count(1)))
                
            graph[i] = [temp] + graph[i]
            
    return min_num
