def insert(a,b):
    c=0
    for i in range(len(a)):
        if a[i]==b[i]:
            c+=1
    c=len(b)-c
    return(c)
a,b=input().split()
if a==b:
    c=0
elif len(a)<=len(b):
    c=insert(a,b)
elif len(a)>len(b):
    c=insert(b,a)
print(c)
