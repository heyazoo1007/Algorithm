import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal = []
for _ in range(n):
    medal.append(list(map(int, input().split())))

# 국가 순서대로 입력되는게 아니라서 0 인덱스를 기준으로 오름차순 정렬 필요함
medal.sort(key = lambda x : x[0])
gold, silver, dong = medal[k-1][1], medal[k-1][2], medal[k-1][3]

medal.sort(key = lambda x : (x[1], x[2], x[3]), reverse = True)


for i in range(n):
    # 목표 국가와 동일한 금은동 가진 국가가 처음으로 나오면 그 인덱스 + 1이 목표 국가의 등수와 동일
    if medal[i][1] == gold and medal[i][2] == silver and medal[i][3] == dong:
        print(i + 1)
        break
    
    
