import sys
input = sys.stdin.readline

n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

answer = []
numbers.sort()
for i in range(1, n - 1):
    median = numbers[i]
    max_avg = numbers[i - 1] + median + numbers[-1]
    min_avg = numbers[0] + median + numbers[i + 1]
    answer.append(max(abs(max_avg - 3 * median), abs(min_avg - 3 * median)))
    
print(max(answer))
