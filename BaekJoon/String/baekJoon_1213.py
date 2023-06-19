from collections import Counter

words = list(input())
words.sort()
words_dic = Counter(words)

first, second = [], []
flag = True
check = True
middle = ''
for each in words_dic.keys():
    
    if words_dic[each] % 2 == 1:
        if flag:
            middle = each
            flag = False
            words_dic[each] -= 1
            while words_dic[each] > 0:
                first.append(each)
                second.append(each)
                words_dic[each] -= 2
        else:
            check = False
            break
                
    else:
        while words_dic[each] > 0:
            first.append(each)
            second.append(each)
            words_dic[each] -= 2
            
           
           
if not check:
    print("I'm Sorry Hansoo")
else:
    first.append(middle)
    print(''.join(first) + ''.join(second[-1::-1]))
