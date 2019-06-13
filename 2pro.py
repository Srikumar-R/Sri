a,b=input().split()
c=0
d=-1
for i in range(int(b)):
    if i%2==0:
        a=a[c+1:]
    if i%2==1:
        a=a[:d]
print(a)
