a,b=input().split()
c=0
if a==b:
    c=0
else:
    for i in range(len(a)):
        if a[i]==b[i]:
            c+=1
    c=len(b)-c
print(c)
