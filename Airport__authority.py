s=[]
for i in range(int(input())):
    b=int(input())
    s.append(b)
a=int(input())
c=0
for i in s:
    if i<=a:
        c+=1
    else:
        c+=2
print(c)