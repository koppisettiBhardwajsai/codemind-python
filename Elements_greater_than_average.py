n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//len(a)
c=0
for i in range(n):
    if a[i]>avg or a[i]==avg:
        c+=1
print(c)