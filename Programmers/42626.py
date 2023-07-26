import heapq

def solution(scoville, K):
    answer = 0 # K를 만들기 위해 섞은 횟수 
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        if first >= K: # 가장 작은 수마저 K이상이므로 모든 수가 K 이상임을 알 수 있음
            break

        result = first + 2 * heapq.heappop(scoville)
        answer += 1
        heapq.heappush(scoville, result)
        
    if scoville[0] < K :
        return -1
    else:
        return answer
