import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    result = [float('inf')] * (N + 1) # 거리 누적 값이 2001보다 클 수 있으므로 inf
    result[1] = 0 # 1번노드에서 1번 노드 거리는 0이다 
    
    for x, y, z in road:
        graph[x].append([y,z])
        graph[y].append([x,z])  
        
    queue = []
    heapq.heappush(queue,[1, 0]) # 노드 번호, 1번부터의 거리
    
    # dijkstra 함수 시작 
    while queue:
        a, b = heapq.heappop(queue)       
        for x,y in graph[a]:
            if b + y < result[x]:
                result[x] = b + y
                heapq.heappush(queue, [x, b + y]) 
    # 함수 끝 
                        
    answer = 0
    for i in range(1, len(result)):
        if result[i] <= K:
            answer += 1
            
    return answer
