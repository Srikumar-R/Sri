def swap(f,k):
    t=f
    f=k
    k=t
    return(f,k)
a=int(input())
b=input().split()
c=[]
d=''
b.sort(key=len)
for i in range(a-1):
    print(b[i])
    if len(b[i])==len(b[i+1]):
        for j in range(len(b[i])):
            if b[i][j]>b[i+1][j]:
                x,y=swap(b[i],b[i+1])
                if x not in c:
                    c.append(x)
                if y not in c:
                    c.append(y)
    elif b[i] not in c:
        c.append(b[i])
if b[-1] not in c:
    c.append(b[-1])
print(c)
