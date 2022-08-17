directory = { 1 : [0,0], 2 : [0,1], 3 : [0,2], 4 : [1,0], 5 : [1,1], 6 :[1,2], 7 : [2,0], 8 : [2,1], 9 : [2,2], '*' : [3,0], 0 : [3,1], '#' : [3,2]}

def solution(numbers, hand):
    answer = ''
    left_distance = 0 
    right_distance = 0 
    hands = {'left' : directory['*'], 'right': directory['#']}
    
    while numbers:
        x = numbers.pop(0)
        if x in [1,4,7]:
            answer += 'L'
            hands['left'] = directory[x]
        elif x in [3,6,9]:
            answer += 'R'
            hands['right'] = directory[x]
        elif x in [2,5,8,0]:
            left_distance = abs(directory[x][0] - hands['left'][0]) + abs(directory[x][1] - hands['left'][1])
            right_distance = abs(directory[x][0] - hands['right'][0]) + abs(directory[x][1] - hands['right'][1])
            
            if left_distance < right_distance:
                answer += 'L'
                hands['left'] = directory[x]
            elif left_distance > right_distance:
                answer += 'R'
                hands['right'] = directory[x]  
            else:
                if hand == 'right':
                    answer += 'R'
                    hands['right'] = directory[x]
                else:
                    answer += 'L'
                    hands['left'] = directory[x]
            
    return answer
