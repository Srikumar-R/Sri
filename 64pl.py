a,b=input().split()
c=input().split()
d=[]
for i in c:
    if int(i)<int(b):
        d.append(i)
d.sort(key=int)
e=''
for i in range(len(d)-1):
    e+=d[i]+" "
print(e+d[-1])
