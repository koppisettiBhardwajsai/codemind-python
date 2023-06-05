n=input()
l=n.split()
for i in range(0,len(l)):
    s=str(l[i])
    if i==0 or i%2==0:
        print(s[-1::-1],end=" ")
    else:
        print(s,end=" ")