n=int(input())
r=0
p=1
while(n>0):
    s=n%10
    r=r+s
    p=p*s
    n=n//10
if r==p:
    print('Spy Number')
else:
    print('Not Spy Number')