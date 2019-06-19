a=int(input())
b=input().split()
c=[]
s=''
for i in range(a):
    if i%2==0 and int(b[i])%2==1:
        c.append(b[i])
    if i%2==1 and int(b[i])%2==0:
        c.append(b[i])
for i in range(len(c)-1):
    s+=c[i]+" "
print(s+c[-1])
