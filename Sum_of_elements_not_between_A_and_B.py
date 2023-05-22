n=int(input())
a=list(map(int,input().split()))
z,x=map(int,input().split())
s=0
for i in a:
    if i<z or i>x:
        s+=i
print(s)