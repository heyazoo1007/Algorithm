import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[-1] * m for _ in range(n)]

for i in range(n):
    temp = list(input())
    for j in range(m):
        if temp[j] == 'c':
            matrix[i][j] = 0

for i in range(n):
    count = 0
    flag = False
    for j in range(m):
        if matrix[i][j] == 0:
            count = 0
            flag = True
            continue
        else:
            if flag :
                count += 1
                matrix[i][j] = count
        

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]), end = ' ')
    print()
