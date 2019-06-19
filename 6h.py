a=int(input())
b=input()
c=''
for i in b:
    if i in c and i!=" ":
        print(int(i))
        break
    else:
        c+=i
if c==b:
    print("unique")
