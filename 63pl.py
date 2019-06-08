a=int(input())
b=input().split()
c=input().split()
d=[]
e=''
for i in b:
    if i in c:
        d.append(i)
        c.remove(i)
for i in range(len(d)-1):
    e+=d[i]+" "
print(e+d[-1])
