import sys
input = sys.stdin.readline

n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))
    
numbers.sort()
answer = -1
for i in range(n - 1, 1, -1): # 삼각형의 가장 긴변 후보는 n - 1 부터 2번 인덱스까지
    first, second, third = numbers[i - 2], numbers[i - 1], numbers[i]
    if third < second + first:
        answer = third + second + first
        break

print(answer)
    
    
