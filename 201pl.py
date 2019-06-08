def fact(x):
  y=1
  for i in range(1,x+1):
    y*=i
  return(y)
a=int(input())
b=[]
c=''
for i in range(a+1):
  b.append(fact(2*i)//(fact(i+1)*fact(i)))
for i in range(len(b)-1):
  c+=str(b[i])+" "
print(c+str(b[-1]))
