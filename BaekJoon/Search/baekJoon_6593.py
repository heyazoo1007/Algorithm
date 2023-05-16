def bfs(c, a, b, matrix, visit, z, x, y):
    visit[c][a][b] = 1
    queue = [[c, a, b]]
    dc, da, db = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
    e, f, g = len(matrix), len(matrix[0]), len(matrix[0][0])
    
    while queue:
        c, a, b = queue.pop(0)
        
        if c == z and a == x and b == y:
            return visit[z][x][y]
        
        for i in range(6):
            nc, na, nb = c + dc[i], a + da[i], b + db[i]
            if 0 <= nc < e and 0 <= na < f and 0 <= nb < g:
                if not visit[nc][na][nb] :
                    if (matrix[nc][na][nb] == '.' or matrix[nc][na][nb] == 'E'):
                        visit[nc][na][nb] = visit[c][a][b] + 1
                        queue.append([nc, na, nb])
                        
    return visit[z][x][y]                   
    
while True:
    first, second, third = map(int, input().split())
    
    if first == 0 and second == 0 and third == 0:
        break
    
    c, a, b = 0, 0, 0
    z, x, y = 0, 0, 0
    matrix = [[] for _ in range(first)]
    for i in range(first):
        for j in range(second + 1): # 한 층 다음에 오는 빈칸 때문에 IndexError 계속 발생함
            temp = list(input())
            if len(temp) != 0:
                matrix[i].append(temp)
            else:
                continue
                 
    times = 0
    for i in range(first):
        for j in range(second):
            for k in range(third):
                if times == 2:
                    break
                if matrix[i][j][k] == 'S':
                    c, a, b = i, j, k # z, x, y
                    times += 1
                if matrix[i][j][k] == 'E':
                    z, x, y = i, j, k
                    times += 1   
    
    visit = [[[0] * third for _ in range(second)] for _ in range(first)]
    answer = bfs(c, a, b, matrix, visit, z, x, y)
    
    if answer == 0:
        print('Trapped!')
    else:
        print('Escaped in ' + str(answer - 1) + ' minute(s).')
