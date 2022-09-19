def solution(priorities, location):    
    
    for i in range(len(priorities)):
        priorities[i] = (i, priorities[i]) #번호, 중요도
        
    
    count = 0
    while True:
        value = priorities.pop(0)
        flag = True
        for i in range(len(priorities)):
            #더 중요한 프린트물이 뒤에 있다 
            if value[1] < priorities[i][1]:
                priorities.append(value)
                flag = False 
                break
        #가장 중요한 프린트물이 가장 첫번째일 때 
        if flag:
            count += 1
            if value[0] == location:
                return count
