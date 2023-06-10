n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]!=0 and a[i]!=1:
        c+=1
        break
if  c>0:
    print(False)
else:
    print(True)