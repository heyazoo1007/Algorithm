word = input()

# replace한 문자열을 다시 word에 저장해야지 틀리지 않는다
word = word.replace('XXXX', 'AAAA')
word = word.replace('XX', 'BB')

if word.count('X') > 0:
    print(-1)
else:
    print(word)
