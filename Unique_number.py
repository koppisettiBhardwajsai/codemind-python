n=int(input())
a=[]
while n!=0:
    r=n%10
    a.append(r)
    n//=10
f=list(set(a))
if len(a)==len(f):
    print('Unique Number')
else:
    print('Not Unique Number')