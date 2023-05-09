import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 누적합 계산 하는 2차 행렬  
fast_sum = [[0] * m for _ in range(n)]  
for x in range(n):
    for y in range(m):
        if x == 0 and y == 0:
            fast_sum[x][y] = matrix[x][y]
        elif x == 0 and y != 0:
            fast_sum[x][y] = matrix[x][y] + fast_sum[x][y - 1]
        elif x != 0 and y == 0:
            fast_sum[x][y] = matrix[x][y] + fast_sum[x - 1][y]
        else:
            fast_sum[x][y] = matrix[x][y] + fast_sum[x - 1][y] + fast_sum[x][y - 1] - fast_sum[x - 1][y - 1]        
        
k = int(input())
for _ in range(k):
    a, b, c, d = map(int, input().split())
    i, j, x, y = a - 1, b - 1, c - 1, d - 1 
    
    if i == 0 and j == 0:
        print(fast_sum[x][y])
    elif i == 0 and j != 0:
        print(fast_sum[x][y] - fast_sum[x][j - 1])
    elif i != 0 and j == 0:
        print(fast_sum[x][y] - fast_sum[i - 1][y])
    elif i != 0 and j != 0: 
        print(fast_sum[x][y] - fast_sum[x][j - 1] - fast_sum[i - 1][y] + fast_sum[i - 1][j - 1])
