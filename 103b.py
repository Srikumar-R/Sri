a=input().split()
j=0
b=[]
c=''
for i in range(len(a)):
    if a[i][j].islower():
        b.append(a[i][j].upper())
for i in range(len(a)-1):
    if b!=[]:
        c+=b[i]+a[i][1:]+" "
    else:
        c+=a[i]+" "
if b!=[]:
    print(c+b[-1]+a[-1][1:])
else:
    print(c+a[-1])
