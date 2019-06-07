a=input()
b=[]
c=''
for i in a:
    b.append(i)
b.reverse()
for i in range(len(b)):
    c+=b[i]
print(c)
