n = int(input())

arr = list(map(int, input().split()))
answer = [0 for _ in range(n)]

for i in range(n):
    count = 0
    for j in range(n):
        if count == arr[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0 : # count != arr[i]
            count += 1

print(' '.join(map(str, answer)))
