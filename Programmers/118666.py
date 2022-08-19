def count(dictionary):
    temp = []
    for i in dictionary.keys():
        temp.append(i)
        
    result = ''
    if dictionary[temp[0]] > dictionary[temp[1]]:
        result += temp[0]
    elif dictionary[temp[0]] < dictionary[temp[1]]:
        result += temp[1]
    else:
        result += temp[0]
    return result
                    
def solution(survey, choices):
    answer = ''
    first = {"R" : 0, "T" : 0}
    second = {"C" : 0, "F" : 0}
    third = {"J" : 0, "M" : 0}
    fourth = {"A" : 0, "N" : 0}
    
    for i in range(len(survey)):
        temp = list(survey[i])
        x,y = temp[0], temp[1]
        num = abs(choices[i] - 4)
        if 1 <= choices[i] <= 3:
            if x in first:
                first[x] += num
            elif x in second:
                second[x] += num
            elif x in third:
                third[x] += num
            elif x in fourth:
                fourth[x] += num
            
        elif choices[i] == 4:
            continue
            
        elif 5 <= choices[i] <= 7:
            if y in first:
                first[y] += num
            elif y in second:
                second[y] += num
            elif y in third:
                third[y] += num
            elif y in fourth:
                fourth[y] += num
                
    answer += count(first)
    answer += count(second)
    answer += count(third)
    answer += count(fourth)
                                    
    return answer
