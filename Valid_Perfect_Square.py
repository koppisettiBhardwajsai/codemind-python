n=int(input())
for i in range(0,n):
    a=int(input())
    s=int(a**0.5)
    sq=s*s
    if sq==a:
        print(True)
    else:
        print(False)