a,b=input().split()
c=input().split()
i=0
while i<int(a):
    if int(c[i])==int(b):
        print(i+1)
        break
    i+=1
