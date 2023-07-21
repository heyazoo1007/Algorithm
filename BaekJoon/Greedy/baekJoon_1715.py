import sys
import heapq
input = sys.stdin.readline

cards = []
for _ in range(int(input())):
    cards.append(int(input()))

heapq.heapify(cards)
answer = 0
while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    
    result = first + second
    heapq.heappush(cards, result)
    answer += result
    
print(answer)
    
