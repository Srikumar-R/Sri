a=int(input())
b=input().split()
c=0
i=0
while i<len(b):
    j=i+1
    while j<len(b):
        if int(b[i])<int(b[j]):
            c+=1
        j+=1
    i+=1
print(c)
