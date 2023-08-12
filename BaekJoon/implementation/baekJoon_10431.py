import sys

for _ in range(int(input())):
    answer = 0
    given = list(map(int, input().split()))
    number, arr = given[0], given[1:]
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                answer += 1
                
    print(number, answer)
