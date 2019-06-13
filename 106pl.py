a=int(input())
b=input().split()
c=[]
d=''
for i in b:
    if i not in c:
        c.append(i)
for i in range(len(c)-1):
    d+=c[i]+" "
print(d+c[-1])
