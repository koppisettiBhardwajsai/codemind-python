def add_digits(n):
    while n>10:
        s=0
        while n>0:
            r=n%10
            s+=r
            n//=10
        n=s
    return n
    
n=int(input())
g=add_digits(n)
print(g)