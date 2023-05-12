n, k = map(int, input().split())

# n에서 k까지 가는 최소 시간
number = 10 ** 5
visit = [[-1, 0] for _ in range(number + 1)]

queue = [n]
visit[n][0] = 0
visit[n][1] = 1
while queue:
    x = queue.pop(0)
        
    for nx in [x - 1, x + 1, 2 * x]:
        if 0 <= nx <= number:
            if visit[nx][0] == -1:
                visit[nx][0] = visit[x][0] + 1
                visit[nx][1] = visit[x][1]
                queue.append(nx)
            elif visit[nx][0] == visit[x][0] + 1:
                visit[nx][1] += visit[x][1]
            
print(visit[k][0])
print(visit[k][1])
