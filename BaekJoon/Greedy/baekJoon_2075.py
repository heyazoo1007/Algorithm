import heapq

n = int(input())
heap = []

for _ in range(n):
    temp = map(int, input().split())
    for each in temp:
        if len(heap) < n:
            heapq.heappush(heap, each)
        else:
            if heap[0] < each:
                heapq.heappop(heap)
                heapq.heappush(heap, each)
                
print(heap[0])
