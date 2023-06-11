n=input()
c=0
v=0
for i in n:
    if i=='z':
        c+=1
    else:
        v+=1
if 2*c==v:
    print('Yes')
else:
    print('No')