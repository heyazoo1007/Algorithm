def solution(dirs):
    #(from, to) 
    routes = []
    directions = {'U': (0, 1), 'D': (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
    dirs = list(dirs)
    
    count = 0
   
    x,y = 0,0
    while dirs:        
        d = dirs.pop(0)
        nx, ny = x + directions[d][0], y + directions[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if [(x,y), (nx,ny)] not in routes:
                count += 1
            routes.append([(x,y), (nx, ny)])     
            routes.append([(nx, ny), (x,y)]) 
            x, y = nx,ny
        else:
            nx, ny = x, y
            continue
    
    return count
