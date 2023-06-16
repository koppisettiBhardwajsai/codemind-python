n=int(input())
for i in range(n):
    a=int(input())
    t=a
    rev=0
    while(a>0):
        r=a%10
        rev=rev*10+r
        a//=10
    if rev==t:
        print(True)
    else:
        print(False)