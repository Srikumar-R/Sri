u,v=input().split()
c=0
d=-1
for i in range(int(v)):
    if i%2==0:
        u=u[c+1:]
    if i%2==1:
        u=u[:d]
print(u)
