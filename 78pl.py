a,b=input().split()
c=input().split()
d=input().split()
c=c+d
c.sort(key=int)
d=''
for i in range(len(c)-1):
    d+=c[i]+" "
print(d+c[-1])
