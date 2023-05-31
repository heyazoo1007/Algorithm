a, b, target_a, target_b = map(int, input().split())

queue = [[0, 0, 0]] # a에 있는 물의 양, b에 있는 물의 양, 연산횟수
visit = set()
visit.add((0, 0))

answer = -1
while queue:
    x, y, times = queue.pop(0)
    
    if x == target_a and y == target_b:
        answer = times
        break
    
    if (a, y) not in visit:
        visit.add((a, y))
        queue.append([a, y, times + 1])
    if (x, b) not in visit:
        visit.add((x, b))
        queue.append([x, b, times + 1])
    if (0, y) not in visit:
        queue.append([0, y, times + 1])
        visit.add((0, y))
    if (x, 0) not in visit:
        queue.append([x, 0, times + 1])
        visit.add((x, 0))
    
    if x + y >= b:
        if (x - b + y, b) not in visit:
            visit.add((x + y - b, b))
            queue.append([x + y - b, b, times + 1])
    else:
        if (0, x + y) not in visit:
            visit.add((0, x + y))
            queue.append([0, x + y, times + 1])

    if x + y >= a:
        if (a, x + y - a) not in visit:
            queue.append([a, x + y - a, times + 1])
            visit.add((a, x + y - a))
    else:
        if (x + y, 0) not in visit:
            queue.append([x + y, 0, times + 1])
            visit.add((x + y, 0))
            
print(answer)
            
