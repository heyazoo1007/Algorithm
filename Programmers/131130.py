def solution(cards):
    n = len(cards)
    for i in range(n):
        cards[i] -= 1
        
    box_set = []
    visit = [0] * n
    for i in range(n):
        if not visit[i]:
            visit[i], count, index = 1, 1, cards[i]
            while True:
                if visit[index]:
                    box_set.append(count)
                    break
                visit[index] = 1
                count += 1
                index = cards[index]            
    box_set.sort(reverse = True)
    
    if len(box_set) == 1:
        return 0
    else:
        return box_set[0] * box_set[1]
