a,b=input().split()
c=0
for i in a:
    if i in b:
        print("yes")
        break
    else:
        c+=1
if c>0:
    print("no")
