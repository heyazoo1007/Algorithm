n = int(input())
arr = input().rstrip().split('*')
first_length = len(arr[0])
second_length = len(arr[1])

for _ in range(n):
    word = input().rstrip()
    length = len(list(word))
    
    # 키워드는 a*a인데 단어는 a인 경우를 거르기 위해서
    if first_length + second_length > length:
        print('NE')
        continue
    
    if arr[0] == word[:first_length] and arr[1] == word[length - second_length : ]:
        print('DA')
    else:
        print('NE')
