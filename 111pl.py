a,b=input().split()
c=input().split()
d=c[:int(a)]
e=c[int(a):]
c=[]
a=''
for i in d:
    if i in e:
        if i not in c:
            c.append(i)
for i in range(len(c)-1):
    a+=c[i]+" "
print(a+c[-1])
