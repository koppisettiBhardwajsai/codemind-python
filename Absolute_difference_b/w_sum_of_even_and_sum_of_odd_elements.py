n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    if i%2==0:
        s+=i
    else:
        c+=i
print(abs(s-c))