from collections import deque
import heapq

def solution(operations):
    heap = []
    max_heap = []
    operations = deque(operations)
    
    while operations:
        op, number = operations.popleft().split()
        
        if op == 'I':
            number = int(number)
            heapq.heappush(heap, number)
            heapq.heappush(max_heap, (-1 * number, number))
        else:
            if len(heap) == 0:
                continue
            if number == '1': 
                x = heapq.heappop(max_heap)[1]
                heap.remove(x)
            elif number == '-1': 
                x = heapq.heappop(heap)
                max_heap.remove((-1 * x, x))
                    
    if len(heap) == 0:
        return [0, 0]
    else:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
                                    
