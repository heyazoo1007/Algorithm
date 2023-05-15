from collections import deque

n, k = map(int, input().split())

number = 2 * 10 ** 5
arr = [0] * (number + 1)
arr[n] = 1

queue = deque()
queue.append(n)
while queue:
    x = queue.popleft()
    
    if x == k:
        break
    
    for nx in [x + 1, x - 1, 2 * x]:
        if 0 <= nx <= 10 ** 5:
            if not arr[nx]:
                if nx == 2 * x:
                    arr[nx] = arr[x]
                else:
                    arr[nx] = arr[x] + 1
                queue.append(nx)
            else:
                if nx == 2 * x:
                    arr[nx] = min(arr[nx], arr[x])
                else:
                    arr[nx] = min(arr[nx], arr[x] + 1)
            
print(arr[k] - 1)
