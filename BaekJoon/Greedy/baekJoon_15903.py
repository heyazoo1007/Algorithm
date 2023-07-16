import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

while m > 0 :
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    
    heapq.heappush(cards, first + second)
    heapq.heappush(cards, first + second)
    
    m -= 1
    
print(sum(cards))
    
