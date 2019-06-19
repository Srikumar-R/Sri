a=input().split()
b=''
for i in a:
    for y in range(-1,-len(i)-1,-1):
        b+=i[y]
    if i!=a[-1]:
        b+=" "
print(b)
