def reverse(number):
    return abs(number - 1)


n = int(input())
switches = [0] + list(map(int, input().split()))

for _ in range(int(input())):
    gender, number = map(int, input().split())
    
    # 남자면 number의 배수만 상태 변경
    if gender == 1: 
        for i in range(number, n + 1):
            if i % number == 0:
                switches[i] = reverse(switches[i])
                
    # 여자인 경우는 양쪽으로 가면서 스위치 타입이 같아야 함           
    else: 
        switches[number] = reverse(switches[number])
        before_index = number - 1
        after_index = number + 1
        while before_index >= 1 and after_index <= n:
            if switches[before_index] != switches[after_index]:
                break
            switches[before_index] = reverse(switches[before_index])
            switches[after_index] = reverse(switches[after_index])
            before_index -= 1
            after_index += 1

m = len(switches)
# 20개를 기준으로 줄바꿈 해야함
for i in range(1, len(switches)):
    print(switches[i], end = ' ')
    if i % 20 == 0 :
        print()
