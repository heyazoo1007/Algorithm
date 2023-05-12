from collections import deque

n, k = map(int, input().split())

number = 10 ** 5
arr = [0 for _ in range(number + 1)]
arr[n] = 1
queue = deque()
queue.append(n)
while queue:
    x = queue.popleft()
    if x == k :
        print(arr[x] - 1)
        break
        
    for i in [x - 1, x + 1, 2 * x]:
        nx = i
        if 0 <= nx <= number and arr[nx] == 0:
            arr[nx] = arr[x] + 1
            queue.append(nx)
