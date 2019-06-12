a=int(input())
b=input().split()
c=1
d=[]
for i in range(len(b)-1):
    if int(b[i])<int(b[i+1]):
        c+=1
    else:
        c=1
    d.append(c)
print(max(d))
