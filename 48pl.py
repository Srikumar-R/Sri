a=int(input())
b=[]
c=''
for i in range(1,a+1):
    if a%i==0 and i%2==1:
        b.append(i)
for i in range(len(b)-1):
    c+=str(b[i])+" "
print(c+str(b[-1]))
