a=int(input())
c=input()
b=c.split()
d=c.split()
e=[]
f=''
b.sort(key=int)
for i in range(len(b)):
    e.append(b.index(d[i])+1)
for i in range(len(e)-1):
    f+=str(e[i])+" "
print(f+str(e[-1]))
