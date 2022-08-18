data = input()
i = 0
check_list = ['U','C','P','C']
for a in check_list:
    if a in data:
        i += 1
        idx = data.index(a)
        data = data[idx+1:]
    else:
        print('I hate UCPC')
        break
if i == 4:
    print('I love UCPC')
