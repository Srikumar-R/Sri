a,b=input().split()
c=input().split()
i=0
while i<len(c):
    j=i+1
    while j<len(c):
        if int(c[i])+int(c[j])==int(b) or b in c:
            k=True
            break
        else:
            k=False
        j+=1
    i+=1
if k==True:
    print("yes")
else:
    
    print("no")
