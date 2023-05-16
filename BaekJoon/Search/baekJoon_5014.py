building, current, company, u, d = map(int, input().split())

arr = [0] * (building + 1)
arr[current] = 1
queue = [current]
while queue:
    x = queue.pop(0)
    
    if x == company:
        break
        
    for nx in [x + u, x - d]:
        if 1 <= nx <= building :
            if not arr[nx]:
                arr[nx] = arr[x] + 1
                queue.append(nx)
            
if arr[company] == 0:
    print("use the stairs")
else:
    print(arr[company] - 1)
