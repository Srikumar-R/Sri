a=int(input())
b=input().split()
c=0
for i in range(a-1):
    c+=int(b[i])+int(b[i+1])
print(c)
