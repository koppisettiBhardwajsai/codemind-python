n=input()
l=n.split()
for i in range(-1,len(l)-2*len(l)-1,-1):
    s=str(l[i])
    print(s[-1::-1],end=" ")