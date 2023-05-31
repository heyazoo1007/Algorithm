from collections import deque

puzzle = ""
for i in range(3):
    puzzle += ''.join(list(input().split()))
    
visit = {puzzle : 0}
queue = deque()
queue.append(puzzle)
answer = -1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while queue:
    puzzle = queue.popleft()
    count = visit[puzzle]
    z = puzzle.index('0')
    
    if puzzle == '123456780':
        answer = count
        
    x, y = z // 3, z % 3
    
    count += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            nz = nx * 3 + ny
            puzzle_list = list(puzzle)
            puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]
            new_puzzle = ''.join(puzzle_list)
            
            if new_puzzle not in visit.keys():
                visit[new_puzzle] = count
                queue.append(new_puzzle)
                
print(answer)
