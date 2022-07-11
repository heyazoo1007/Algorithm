n=int(input())
a,b,c,d,e,f=map(int,input().split())
data=[a,b,c,d,e,f]
z=min(data)
y=min(a+b,a+e,a+c,a+d,b+f,b+d,b+c,c+e,c+f,d+e,d+f,e+f)
x=min(b+c+f,b+d+f,d+e+f,c+e+f,a+c+e,a+b+c,a+d+e,a+b+d)

if n==1:
    print(sum(data)-max(data))
elif n==2:
    print(x*4+y*4)
else:     
    three=x*4
    two=4*y*(2*n-3)
    one=z*(5*n*n+(-16)*n+12)

    print(one+two+three)
