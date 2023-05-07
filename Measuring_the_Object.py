w,x,y,z=map(int,input().split())
if x+y==w or y+z==w or x+z==w:
    print('YES')
elif x==w or y==w or z==w:
    print('YES')
else:
    print('NO')