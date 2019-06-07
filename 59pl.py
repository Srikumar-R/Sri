a=int(input())
b=input().split()
c=[]
d=''
if b.count("0")>0:
    for i in b:
        if i!="0":
            c.append(i)
        else:
            break
    if c!=[]:
        for i in range(len(c)-1):
            d+=c[i]+" "
    if c!=[]:
        print(d+c[-1])
