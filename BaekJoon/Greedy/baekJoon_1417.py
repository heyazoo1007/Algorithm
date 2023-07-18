import heapq

n = int(input())

first = -1 * int(input())
votes = []
for i in range(1, n):
    votes.append([-1 * int(input()), i])

heapq.heapify(votes)

count = 0
while votes:
    vote_num, number = heapq.heappop(votes)
    
    if vote_num > first: # 1번 득표수가 제일 큼
        break
        
    heapq.heappush(votes, [vote_num + 1, number])
    first -= 1
    count += 1
    
print(count)
        
    
