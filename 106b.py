u,v=input().split()
a=input().split()
b=[]
for i in a:
    if int(i)%2==1:
        b.append(i)
print(b[int(v)-1])
