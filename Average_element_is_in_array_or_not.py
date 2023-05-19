n=int(input())
k=list(map(int,input().split()))
s=0
for i in k:
    s+=i
a=s//n
if a in k:
    print(True)
else:
    print(False)