a=int(input())
b=input().split()
c=[]
d=[]
for i in range(len(b)):
    if int(b[i])%2==0:
        c.append(b[i])
    else:
        d.append(b[i])
if len(c)==1:
    print(c[0])
else:
    print(d[0])
