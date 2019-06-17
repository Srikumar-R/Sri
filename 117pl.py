a=input()
b=''
for i in range(1,len(a)):
    b+=a[-i]+"-"
print(b+a[0])
