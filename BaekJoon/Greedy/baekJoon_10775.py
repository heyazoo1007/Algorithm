import sys
input=sys.stdin.readline

answer=0
g=int(input())
p=int(input())
planes=[]
parent=[i for i in range(g+1)]

for _ in range(p):
    planes.append(int(input()))

def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

for plane in planes: #각 비행기의 게이트 번호
    docking=find(plane)
    if docking == 0: #도킹할 수 있는 게이트가 없는 경우
        break
    #해당 비행기와 게이트는 도킹했다는 것을 나타내기 위함
    parent[docking]=parent[docking-1]
    answer+=1
    
print(answer)
