a=int(input())
b=input().split()
d=0
e=[]
f=''
for i in range(a):
    c=b[i:]
    for y in range(len(c)):
        d+=int(c[y])
    e.append(d)
    d=0
for i in range(len(e)-1):
    f+=str(e[i])+" "
print(f+str(e[-1]))
