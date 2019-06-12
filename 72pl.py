a=int(input())
b=input().split()
i=0
while int(b[i])<=int(b[i+1]):
    c=b[i+1]
    i+=1
print(c)
