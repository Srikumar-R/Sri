a,b,c=input().split()
d=0
e=0
while d<int(c):
    e+=int(a)
    a=int(a)+int(b)
    d+=1
print(e)
