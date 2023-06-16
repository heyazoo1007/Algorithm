from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w = input().rstrip()
    k = int(input())
    
    count_char_dict = Counter(list(w))
    
    check = False
    max_answer = -1
    min_answer = len(w)
    check_dict = {} # 특정 문자열의 index를 저장하는 딕셔너리 
    
    for i in range(len(w)):
        if count_char_dict[w[i]] < k:
            continue
            
        check = True
        check_dict[w[i]] = check_dict.get(w[i], []) + [i]
        
    for key, value_list in check_dict.items(): # 알파벳, 인덱스 리스트 
        for i in range(len(value_list) - k + 1):
            max_answer = max(max_answer, value_list[i + k - 1] - value_list[i] + 1)
            min_answer = min(min_answer, value_list[i + k - 1] - value_list[i] + 1)
            
    if check :
        print(min_answer, max_answer) 
    else:
        print(-1)
