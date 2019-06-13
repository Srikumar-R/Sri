a,b=input().split()
c=0
for i in range(int(b)+1):
    if str(i) in a:
        c+=1
if c>int(b):
    print('yes')
else:
    print('no')
