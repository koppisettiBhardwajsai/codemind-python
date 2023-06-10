n=int(input())
a=list(map(int,input().split()))
m,b=map(int,input().split())
s=[]
c=0
for i in a:
    if i<m or i>b:
        s.append(i)
        c+=1
if c>0:
    print(max(s))
else:
    print(-1)