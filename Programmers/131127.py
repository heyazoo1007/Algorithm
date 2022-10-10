def solution(want, number, discount):
    answer = 0
    x, y = sum(number), len(discount)
    want_dict = {want[i] : number[i] for i in range(len(want))}
    
    days = 0
    for i in range(y - x + 1):
        temp_dict = {}
        for j in range(i, i + x):
            if discount[j] in temp.keys():
                temp_dict[discount[j]] += 1
            else:
                temp_dict[discount[j]] = 1
                
        if temp == want_dict :
            days += 1
            
    return days
