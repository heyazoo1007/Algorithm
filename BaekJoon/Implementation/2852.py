from datetime import datetime 

n = int(input())
start_time = datetime.strptime('00:00', "%M:%S")
end_time = datetime.strptime('48:00', "%M:%S")

scores = [ start_time for _ in range(2)]
winning = 0
post_time = start_time
for i in range(n):
    number, time = input().split()
    number = int(number) - 1
    current_time = datetime.strptime(time, "%M:%S")
    
    if i == n - 1:
        scores[number] +=  end_time - current_time
        break
    
    if winning == number: 
        scores[number] +=  current_time - post_time  
    else: # 이전에 이기던 시간은 끝남, 그것도 더해줘야지
        scores[number] += current_time - post_time
        winning = number
        post_time = current_time
        
print(scores[0].strftime('%M:%S'))
print(scores[1].strftime('%M:%S'))
        
