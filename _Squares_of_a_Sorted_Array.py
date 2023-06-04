n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    s.append(i**2)
s.sort()
for j in s:
    print(j,end=" ")