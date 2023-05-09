import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

fast_sum = [0] * n
fast_sum[0] = arr[0]
for i in range(1, n):
    fast_sum[i] += arr[i] + fast_sum[i - 1]

count = {} # 내 앞에 target 값이 몇 개 있는지 확인하는 딕셔너리    
answer = 0
for i in range(n):
    target = fast_sum[i] - k
    
    if target == 0 :
        answer += 1    
    if target in count : 
        answer += count[target]
  
    if fast_sum[i] not in count:
        count[fast_sum[i]] = 0
   
    count[fast_sum[i]] += 1  # fast_sum[i]인 수가 하나 더 들었으니까
            
print(answer)
