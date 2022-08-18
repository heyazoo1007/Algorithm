s=list(input())
t=list(input())

while True:
    if len(t) == len(s) :
        if t ==s :
            print(1)
            break
        else:
            print(0)
            break
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t.reverse()
