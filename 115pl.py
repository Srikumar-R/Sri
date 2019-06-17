a,b=input().split()
c=0
if len(a)==len(b):
    print(a+b)
else:
    m=max(a,b,key=len)
while len(a)!=len(b):
    a=a[:len(a)-1]
    c+=1
if c>0:
    print(a+b)
