n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(0,n):
    c=0
    for j in a:
        if a[b]>j:
            c+=1
    print(c,end=" ")
    b+=1