a,b=input().split()
c=input().split()
for i in range(int(b)):
    d=max(c,key=int)
    c.pop(c.index(max(c,key=int)))
print(d)
