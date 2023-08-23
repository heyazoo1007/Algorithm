import sys 
input = sys.stdin.readline

prices = list(map(int, input().split()))
time = [0] * 101
for i in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i] += 1
        
answer = 0        
for i in range(101):
    answer += time[i] * prices[time[i] - 1]
    
print(answer)
    
