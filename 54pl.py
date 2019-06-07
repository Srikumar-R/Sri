a,b=input().split()
c=0
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]==b[i]:
            c+=1
    if c==len(b):
        print("yes")
    else:
        print("no")
else:
    print("no")
