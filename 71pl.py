a=int(input())
b=input().split()
c=[]
d=''
for i in range(len(b)-1):
    if int(b[i])>=int(b[i+1]):
        c.append(b[i])
    else:
        c.append(b[i+1])
for i in range(len(c)-1):
    d+=c[i]+" "
print(d+c[-1])
