a,b=input().split()
i=0
c=1
while i<int(b):
    c*=int(a)
    a=int(a)-1
    i+=1
print(c)
