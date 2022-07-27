from collections import deque

sx,sy=0,0
shark_size=2
time=0
eat_cnt=0
fish_cnt=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(n):
        if 0<data[i][j]<=6:
            fish_cnt+=1
        if data[i][j]==9:
            sx,sy=i,j
data[sx][sy]=0

def bfs(x,y):
    q=deque()
    #상어 x,y,이동한 거리
    q.append((x,y,0))
    visit=[[0]*n for _ in range(n)]
    visit[x][y]=1
    distance=[]
    min_dist=10**9
    while q:
        x,y,dist=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                #상어가 이동할 수 있는 위치인지 확인 
                if data[nx][ny] <=shark_size:
                    visit[nx][ny]=1
                    
                    #먹을 수 있는 물고기가 있는 경우
                    #그 물고기 먹고 이동한 위치와 1칸 이동했으니 +1
                    if 0<data[nx][ny] < shark_size:
                        min_dist=dist
                        distance.append((dist+1,nx,ny))
                    #이동만 할 수 있는 경우
                    if dist+1 <= min_dist :
                        q.append((nx,ny,dist+1))
    if distance:
        distance.sort()
        #가장 가까운 먹을 수 있는 물고기 위치 반환 
        return distance[0]
    else:
        return False

while fish_cnt:
    result=bfs(sx,sy)
    
    if not result: 
        break
        
    sx,sy=result[1],result[2]
    time+=result[0]
    eat_cnt+=1
    fish_cnt-=1
    
    if shark_size == eat_cnt:
        shark_size+=1
        eat_cnt=0
    data[sx][sy]=0
    
print(time)        
                                                                     
