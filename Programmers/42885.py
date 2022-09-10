from collections import deque

def solution(people, limit):
    people.sort()
    answer = 0 
    people = deque(people)
    
    while people:
        if len(people) == 1:
            answer += 1
            break
        #가장 무거운 사람과 가장 가벼운 사람이 탈 수 있을 때
        elif people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        #가장 무거운 사람이 하나의 보트만 탄다
        else:
            answer += 1
            people.pop()
            
    return answer
            
   
    
    
    
