n=input()
l=n.split()
for i in l:
    s=str(i)
    print(s[-1::-1],end=" ")