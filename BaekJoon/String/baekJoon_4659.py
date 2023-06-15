vowels = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

while True:
    word = input()
    
    if word == 'end':
        break
        
    arr = list(word)
    count = 0
    flag = True
    # 모음 없는 경우와 oo/ee 가 아닌 모음이 두 개 연속되는 단어 있는지 확인
    for vowel in vowels:
        if vowel in arr:
            count += 1
        two = vowel + vowel
        if two in word:
            if two != 'oo' and two != 'ee':
                flag = False
    
    if count == 0 or not flag:
        print('<' + word + '>' + ' is not acceptable.')
        continue

    # 같은 자음 연속으로 두 개 있는지 확인
    for each in consonant:
        if each + each in word:
            flag = False
            print('<' + word + '>' + ' is not acceptable.')
            break
            
    # 연속된 세 알파벳이 모두 자음에 포함되거나 모두 모음에 포함되는 경우 있는지 확인         
    for i in range(0, len(arr) - 2):
        first, second, third = arr[i], arr[i + 1], arr[i + 2]
        if first in vowels and second in vowels and third in vowels:
            flag = False
            print('<' + word + '>' + ' is not acceptable.')
            break
        if first in consonant and second in consonant and third in consonant:
            flag = False
            print('<' + word + '>' + ' is not acceptable.')
            break
            
    if flag : 
        print('<' + word + '>' + ' is acceptable.')
