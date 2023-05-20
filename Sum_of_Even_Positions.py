n=int(input())
r=list(map(int,input().split()))
s=0
for i in range(0,n):
    if i==0 or i%2==0:
        s+=r[i]
print(s)