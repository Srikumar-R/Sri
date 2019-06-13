a,b=input().split()
c=0
for i in range(int(a),int(b)+1):
    if i%2==1:
        c+=i
print(c)
